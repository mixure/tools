require 'find'
dir=Dir.pwd

def source_files dir,sfs
    Dir.glob(File.join(dir,'*')) do |f|
      source_files(f,sfs) if File.directory?(f)
      sfs<< File.join(dir,'*.java') if not sfs.include?(f) and f=~/.java$/
    end
    sfs
end

namespace :admin do
  desc "Compile java source files"
  task :compile do
    sfs=source_files dir,[]
    sfs=sfs.join " "
    %x<javac -d . #{sfs}>
    puts 'done'
  end
end
