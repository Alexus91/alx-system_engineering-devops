#!/usr/bin/env ruby
# Script accepts one argument and passes it to a regular expression,
# Method matching

puts ARGV[0].scan(/^h.n$/).join
