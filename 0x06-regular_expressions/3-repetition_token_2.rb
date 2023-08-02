#!/usr/bin/env ruby
# Accepts one argument and passes it to a regular expression,
# Matching method

puts ARGV[0].scan(/hbt+n/).join
