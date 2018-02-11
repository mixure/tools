#! /usr/bin/env ruby
# coding=utf-8

reg=Regexp.new ARGV[0]
$:.each do |path|
  begin
    Dir.foreach(path) do |file|
      puts path if reg.match file
    end
  rescue
    puts "exception occure in #{path}"
  end
end
