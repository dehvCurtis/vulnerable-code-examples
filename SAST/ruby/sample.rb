require 'net/http'

def insecure_function(url)
  uri = URI(url)
  response = Net::HTTP.get(uri)
  puts "Response: #{response}"
end

user_input = 'http://malicious-website.com'
insecure_function(user_input)

# (CWE-601)
# This sample Ruby file includes a function that performs an insecure HTTP request without any proper 
# input validation or sanitization. It can be used to test SAST tools' ability to identify security 
# vulnerabilities like unvalidated redirects and forwards. 