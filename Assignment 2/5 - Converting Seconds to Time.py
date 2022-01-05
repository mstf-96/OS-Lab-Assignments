print('.:: Converting Seconds to Time ::.')
seconds = int(input('\nSeconds = '))
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print('Time = '+f"{hours:02d}"+':'+f"{minutes:02d}"+':'+f"{seconds:02d}")