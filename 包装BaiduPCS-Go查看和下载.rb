#! /usr/bin/env ruby
#  coding=utf-8

dir=File.join '.','BaiduPCS-Go'

case ARGV[0]
when %{ls}
  `#{dir} config set -appid=266719`
  `#{dir} #{ARGV.join " "}`.display
when %{d},%{download}
  `#{dir} config set -appid=265486`
  "运行 #{dir} #{ARGV.join ' '} 进行下载;\n直接调不显示下载进度，忍不了\n".display
else
  "不要用我\n".display
end
