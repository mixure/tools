# Download the twilio-ruby library from twilio.com/docs/libraries/ruby
require 'twilio-ruby'
require 'open-uri'

account_sid = ''
auth_token = ''
client = Twilio::REST::Client.new(account_sid, auth_token)

from = '' # Your Twilio number
to = '+' # Your mobile phone number

url='http://e.weather.com.cn/mweather15d/101010100.shtml'

r='''
<div class="list-left">
<p class="week">(.+)</p>
<p class="date">(.+)</p>
</div>
<div class="list-right">
<p>
<i class="svnicon housr_icons d01"></i>
<span class="weatherWord">(.+)</span>
<span class="d-temp">(.+)</span>
</p>
<p>
<i class="svnicon housr_icons n01"></i>
<span class="weatherWord">(.+)</span>
<span class="n-temp">(.+)</span>
</p>
</div>
<div class="list-right-wind">
<p class="windD wefther-fx">
<img class=.+ src=.+ alt="">
<br>
<img class=.+ src=.+ alt="">
</p><p class="windS">
<span>(.+)</span><br>
<span>(.+)</span>
</p>
'''

open(url).read=~ Regexp.new(r)
msg= "#{$1}(#{$2}):#{$3},#{$4},#{$7}/#{$5},#{$6},#{$8}"

[
  to # 这是xxx的手机号; 其他接受方也要到twilio做登记...
].each do |receiver|
  client.messages.create(
    from: from,
    to: receiver,
    body: "#{msg}" 
  )
end
