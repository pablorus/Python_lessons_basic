# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева
# и два символа в верхнем регистре справа. Решить задачу двумя способами: с помощью re и без.
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# Задача-3:
# Напишите скрипт заполняющий указанный файл (самомстоятельно задайте имя файла) произвольными целыми
# цифрами, в результате в файле должно быть 2500-значное произвольное число
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле
