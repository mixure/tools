require 'rest-client'

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

r=RestClient.get(url).scan(Regexp.new(r))[1]
msg= "#{r[0]},(#{r[1]})#{r[3]}#{r[4]},#{r[7]},#{r[5]},#{r[6]},#{r[8]}" # 如何插入中文

server_jian="https://sc.ftqq.com/SCU50181T6253d66a03616f402091464e460e01365cc6533cbe0f5.send"
RestClient.post server_jian,{text:'明日天气',desp:msg}
puts msg

# 在微信上会去掉一些字符，如逗号
