def break_lines(in_file_name: str, out_file_name: str, num_chars_per_line: int):
  with open(in_file_name) as without_line_breaks:
    with open(out_file_name, "w") as with_line_breaks:
      line = without_line_breaks.read(num_chars_per_line)
      while line:
        with_line_breaks.write(line)
        with_line_breaks.write('\n')
        line = without_line_breaks.read(num_chars_per_line)
        
        
if __name__ == '__main__':
  in_file_name = 'no_breaks'
  out_file_name = 'breaks'
  num_chars_per_line = 10
  break_lines(in_file_name, out_file_name, num_chars_per_line)
      
