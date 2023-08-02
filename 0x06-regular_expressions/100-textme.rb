#!/usr/bin/env ruby
#Script that matches [SENDER],[RECEIVER],[FLAGS]
#The sender phone number or name (including country code if present
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
