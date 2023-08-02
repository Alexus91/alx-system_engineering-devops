#!/usr/bin/env ruby
# accepts one argument and passes it to a regular expression.
# matching method

puts ARGV[0].scan(/hbt*n/).join
