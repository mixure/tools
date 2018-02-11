#! /usr/bin/env ruby
# coding=utf-8

reg=Regexp.new ARGV[0]
$:.each do |path|
  Dir.foreach(path) do |file|
    puts path if reg.match file
  end
end
