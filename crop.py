#import os
#import datetime
#
#import time
#starttime=time.time()
#while True:
#	os.system("screencapture "+ str(datetime.datetime.now()).replace(' ', '-') + '.png')
#	time.sleep(10.0 - ((time.time() - starttime) % 10.0))

import os
import datetime
from PIL import Image

dates = []

for i in os.listdir('.'):
	date = i.split('.png')[0]
	if date.startswith('2020'):
		date = date[:10] + ' ' + date[11:]
		parsed_date = datetime.datetime.fromisoformat(date)
		dates.append(parsed_date)
	
def crop_image():
	for i in sorted(dates):
		test_image = str(i).replace(' ', '-') + '.png'
		original = Image.open(test_image)
		width, height = original.size   # Get dimensions
		# x_offset, Y_offset, width, height
		#(left, upper, right, lower).
		print(width, height)
		cropped_example = original.crop((0, 359, 3366, 1920))
		cropped_example.save('./cropped/crop_' + str(i) + '.png', 'PNG')


long_or_short = {'2020-05-14 03:01:00': -1, '2020-05-14 03:02:00': -1, '2020-05-14 03:03:00': 0, '2020-05-14 03:04:00': 0, '2020-05-14 03:05:00': 0, '2020-05-14 03:06:00': 0, '2020-05-14 03:07:00': -1, '2020-05-14 03:08:00': -1, '2020-05-14 03:09:00': 0, '2020-05-14 03:10:00': -1, '2020-05-14 03:11:00': 0, '2020-05-14 03:12:00': -1, '2020-05-14 03:13:00': 0, '2020-05-14 03:14:00': -1, '2020-05-14 03:15:00': 0, '2020-05-14 03:16:00': -1, '2020-05-14 03:17:00': 0, '2020-05-14 03:18:00': 1, '2020-05-14 03:19:00': 0, '2020-05-14 03:20:00': 1, '2020-05-14 03:21:00': 0, '2020-05-14 03:22:00': 0, '2020-05-14 03:23:00': 0, '2020-05-14 03:24:00': 0, '2020-05-14 03:25:00': 0, '2020-05-14 03:26:00': 1, '2020-05-14 03:27:00': 0, '2020-05-14 03:28:00': 1, '2020-05-14 03:29:00': 1, '2020-05-14 03:30:00': 0, '2020-05-14 03:31:00': 0, '2020-05-14 03:32:00': 0, '2020-05-14 03:33:00': -1, '2020-05-14 03:34:00': -1, '2020-05-14 03:35:00': 0, '2020-05-14 03:36:00': 0, '2020-05-14 03:37:00': 0, '2020-05-14 03:38:00': 0, '2020-05-14 03:39:00': 0, '2020-05-14 03:40:00': 0, '2020-05-14 03:41:00': 0, '2020-05-14 03:42:00': 0, '2020-05-14 03:43:00': 0, '2020-05-14 03:44:00': -1, '2020-05-14 03:45:00': 0, '2020-05-14 03:46:00': 1, '2020-05-14 03:47:00': 0, '2020-05-14 03:48:00': 0, '2020-05-14 03:49:00': 0, '2020-05-14 03:50:00': 0, '2020-05-14 03:51:00': 0, '2020-05-14 03:52:00': 0, '2020-05-14 03:53:00': 0, '2020-05-14 03:54:00': 0, '2020-05-14 03:55:00': 0, '2020-05-14 03:56:00': 0, '2020-05-14 03:57:00': 0, '2020-05-14 03:58:00': 0, '2020-05-14 03:59:00': 0, '2020-05-14 04:00:00': 0, '2020-05-14 04:01:00': 0, '2020-05-14 04:02:00': 0, '2020-05-14 04:03:00': 0, '2020-05-14 04:04:00': 0, '2020-05-14 04:05:00': 0, '2020-05-14 04:06:00': 0, '2020-05-14 04:07:00': 0, '2020-05-14 04:08:00': 0, '2020-05-14 04:09:00': 0, '2020-05-14 04:10:00': 0, '2020-05-14 04:11:00': -1, '2020-05-14 04:12:00': 0, '2020-05-14 04:13:00': 0, '2020-05-14 04:14:00': 0, '2020-05-14 04:15:00': 0, '2020-05-14 04:16:00': 1, '2020-05-14 04:17:00': 0, '2020-05-14 04:18:00': 0, '2020-05-14 04:19:00': 0, '2020-05-14 04:20:00': 0, '2020-05-14 04:21:00': 0, '2020-05-14 04:22:00': 0, '2020-05-14 04:23:00': 0, '2020-05-14 04:24:00': 0, '2020-05-14 04:25:00': 1, '2020-05-14 04:26:00': 0, '2020-05-14 04:27:00': 0, '2020-05-14 04:28:00': 1, '2020-05-14 04:29:00': 0, '2020-05-14 04:30:00': 0, '2020-05-14 04:31:00': 0, '2020-05-14 04:32:00': 0, '2020-05-14 04:33:00': 0, '2020-05-14 04:34:00': 0, '2020-05-14 04:35:00': 1, '2020-05-14 04:36:00': 1, '2020-05-14 04:37:00': -1, '2020-05-14 04:38:00': 0, '2020-05-14 04:39:00': 0, '2020-05-14 04:40:00': 0, '2020-05-14 04:41:00': 0, '2020-05-14 04:42:00': -1, '2020-05-14 04:43:00': 0, '2020-05-14 04:44:00': 0, '2020-05-14 04:45:00': 0, '2020-05-14 04:46:00': 0, '2020-05-14 04:47:00': 0, '2020-05-14 04:48:00': 0, '2020-05-14 04:49:00': 1, '2020-05-14 04:50:00': 0, '2020-05-14 04:51:00': 0, '2020-05-14 04:52:00': 0, '2020-05-14 04:53:00': 0, '2020-05-14 04:54:00': 0, '2020-05-14 04:55:00': 0, '2020-05-14 04:56:00': 0, '2020-05-14 04:57:00': 0, '2020-05-14 04:58:00': 0, '2020-05-14 04:59:00': 0, '2020-05-14 05:00:00': 0, '2020-05-14 05:01:00': 0, '2020-05-14 05:02:00': 0, '2020-05-14 05:03:00': 0, '2020-05-14 05:04:00': 0, '2020-05-14 05:05:00': 0, '2020-05-14 05:06:00': 0, '2020-05-14 05:07:00': 0, '2020-05-14 05:08:00': 1, '2020-05-14 05:09:00': 0, '2020-05-14 05:10:00': 0, '2020-05-14 05:11:00': 0, '2020-05-14 05:12:00': 0, '2020-05-14 05:13:00': 0, '2020-05-14 05:14:00': 0, '2020-05-14 05:15:00': 0, '2020-05-14 05:16:00': 0, '2020-05-14 05:17:00': 0, '2020-05-14 05:18:00': 0, '2020-05-14 05:19:00': 0, '2020-05-14 05:20:00': 0, '2020-05-14 05:21:00': 0, '2020-05-14 05:22:00': 0, '2020-05-14 05:23:00': 0, '2020-05-14 05:24:00': 0, '2020-05-14 05:25:00': 0, '2020-05-14 05:26:00': 0, '2020-05-14 05:27:00': -1, '2020-05-14 05:28:00': 0, '2020-05-14 05:29:00': 0, '2020-05-14 05:30:00': 1, '2020-05-14 05:31:00': 1, '2020-05-14 05:32:00': 1, '2020-05-14 05:33:00': 0, '2020-05-14 05:34:00': 0, '2020-05-14 05:35:00': -1, '2020-05-14 05:36:00': 0, '2020-05-14 05:37:00': 0, '2020-05-14 05:38:00': 0, '2020-05-14 05:39:00': 0, '2020-05-14 05:40:00': 0, '2020-05-14 05:41:00': 0, '2020-05-14 05:42:00': 0, '2020-05-14 05:43:00': 0, '2020-05-14 05:44:00': 0, '2020-05-14 05:45:00': 1, '2020-05-14 05:46:00': 1, '2020-05-14 05:47:00': 0, '2020-05-14 05:48:00': 0, '2020-05-14 05:49:00': 0, '2020-05-14 05:50:00': 0, '2020-05-14 05:51:00': 0, '2020-05-14 05:52:00': 0, '2020-05-14 05:53:00': 0, '2020-05-14 05:54:00': 0, '2020-05-14 05:55:00': 0, '2020-05-14 05:56:00': -1, '2020-05-14 05:57:00': 0, '2020-05-14 05:58:00': 0, '2020-05-14 05:59:00': 0, '2020-05-14 06:00:00': 0, '2020-05-14 06:01:00': -1, '2020-05-14 06:02:00': 0, '2020-05-14 06:03:00': -1, '2020-05-14 06:04:00': 0, '2020-05-14 06:05:00': 0, '2020-05-14 06:06:00': 0, '2020-05-14 06:07:00': 0, '2020-05-14 06:08:00': -1, '2020-05-14 06:09:00': 0, '2020-05-14 06:10:00': 0, '2020-05-14 06:11:00': -1, '2020-05-14 06:12:00': 0, '2020-05-14 06:13:00': 0, '2020-05-14 06:14:00': 0, '2020-05-14 06:15:00': 1, '2020-05-14 06:16:00': -1, '2020-05-14 06:17:00': -1, '2020-05-14 06:18:00': 0, '2020-05-14 06:19:00': 0, '2020-05-14 06:20:00': 0, '2020-05-14 06:21:00': 0, '2020-05-14 06:22:00': 0, '2020-05-14 06:23:00': 0, '2020-05-14 06:24:00': 0, '2020-05-14 06:25:00': 0, '2020-05-14 06:26:00': -1, '2020-05-14 06:27:00': 0, '2020-05-14 06:28:00': 0, '2020-05-14 06:29:00': 0, '2020-05-14 06:30:00': 0, '2020-05-14 06:31:00': -1, '2020-05-14 06:32:00': 0, '2020-05-14 06:33:00': 0, '2020-05-14 06:34:00': 0, '2020-05-14 06:35:00': 1, '2020-05-14 06:36:00': 0, '2020-05-14 06:37:00': 0, '2020-05-14 06:38:00': 0, '2020-05-14 06:39:00': 1, '2020-05-14 06:40:00': 0, '2020-05-14 06:41:00': 0, '2020-05-14 06:42:00': 0, '2020-05-14 06:43:00': 0, '2020-05-14 06:44:00': 0, '2020-05-14 06:45:00': 0, '2020-05-14 06:46:00': 0, '2020-05-14 06:47:00': 0, '2020-05-14 06:48:00': 0, '2020-05-14 06:49:00': 0, '2020-05-14 06:50:00': 1, '2020-05-14 06:51:00': 0, '2020-05-14 06:52:00': 0, '2020-05-14 06:53:00': 0, '2020-05-14 06:54:00': 0, '2020-05-14 06:55:00': 0, '2020-05-14 06:56:00': 0, '2020-05-14 06:57:00': 0, '2020-05-14 06:58:00': 0, '2020-05-14 06:59:00': 0, '2020-05-14 07:00:00': 0, '2020-05-14 07:01:00': 0, '2020-05-14 07:02:00': 0, '2020-05-14 07:03:00': 0, '2020-05-14 07:04:00': 0, '2020-05-14 07:05:00': 0, '2020-05-14 07:06:00': 0, '2020-05-14 07:07:00': 0, '2020-05-14 07:08:00': -1, '2020-05-14 07:09:00': 0, '2020-05-14 07:10:00': 0, '2020-05-14 07:11:00': 0, '2020-05-14 07:12:00': 0, '2020-05-14 07:13:00': 0, '2020-05-14 07:14:00': 0, '2020-05-14 07:15:00': 0, '2020-05-14 07:16:00': 0, '2020-05-14 07:17:00': 0, '2020-05-14 07:18:00': 0, '2020-05-14 07:19:00': 0, '2020-05-14 07:20:00': 0, '2020-05-14 07:21:00': 0, '2020-05-14 07:22:00': 0, '2020-05-14 07:23:00': 0, '2020-05-14 07:24:00': 0, '2020-05-14 07:25:00': 0, '2020-05-14 07:26:00': 0, '2020-05-14 07:27:00': 0, '2020-05-14 07:28:00': -1, '2020-05-14 07:29:00': 0, '2020-05-14 07:30:00': 0, '2020-05-14 07:31:00': 0, '2020-05-14 07:32:00': 0, '2020-05-14 07:33:00': 0, '2020-05-14 07:34:00': 0, '2020-05-14 07:35:00': 0, '2020-05-14 07:36:00': 0, '2020-05-14 07:37:00': 0, '2020-05-14 07:38:00': 0, '2020-05-14 07:39:00': 0, '2020-05-14 07:40:00': 0, '2020-05-14 07:41:00': 0, '2020-05-14 07:42:00': 0, '2020-05-14 07:43:00': 0, '2020-05-14 07:44:00': 0, '2020-05-14 07:45:00': 0, '2020-05-14 07:46:00': 0, '2020-05-14 07:47:00': 0, '2020-05-14 07:48:00': 0, '2020-05-14 07:49:00': 0, '2020-05-14 07:50:00': 0, '2020-05-14 07:51:00': 0, '2020-05-14 07:52:00': 0, '2020-05-14 07:53:00': 0, '2020-05-14 07:54:00': 0, '2020-05-14 07:55:00': 0, '2020-05-14 07:56:00': 0, '2020-05-14 07:57:00': 0, '2020-05-14 07:58:00': 0, '2020-05-14 07:59:00': 0, '2020-05-14 08:00:00': 1, '2020-05-14 08:01:00': 0, '2020-05-14 08:02:00': 0, '2020-05-14 08:03:00': 0, '2020-05-14 08:04:00': 0, '2020-05-14 08:05:00': 0, '2020-05-14 08:06:00': 0, '2020-05-14 08:07:00': 0, '2020-05-14 08:08:00': 0, '2020-05-14 08:09:00': 1, '2020-05-14 08:10:00': 0, '2020-05-14 08:11:00': 0, '2020-05-14 08:12:00': 0, '2020-05-14 08:13:00': 0, '2020-05-14 08:14:00': 0, '2020-05-14 08:15:00': 0, '2020-05-14 08:16:00': 0, '2020-05-14 08:17:00': 0, '2020-05-14 08:18:00': 0, '2020-05-14 08:19:00': 0, '2020-05-14 08:20:00': 0, '2020-05-14 08:21:00': 0, '2020-05-14 08:22:00': 0, '2020-05-14 08:23:00': 0, '2020-05-14 08:24:00': 0, '2020-05-14 08:25:00': 1, '2020-05-14 08:26:00': 0, '2020-05-14 08:27:00': 0, '2020-05-14 08:28:00': 0, '2020-05-14 08:29:00': 0, '2020-05-14 08:30:00': 1, '2020-05-14 08:31:00': -1, '2020-05-14 08:32:00': 0, '2020-05-14 08:33:00': 0, '2020-05-14 08:34:00': 0, '2020-05-14 08:35:00': 0, '2020-05-14 08:36:00': 0, '2020-05-14 08:37:00': 0, '2020-05-14 08:38:00': 0, '2020-05-14 08:39:00': 0, '2020-05-14 08:40:00': 0, '2020-05-14 08:41:00': 0, '2020-05-14 08:42:00': 0, '2020-05-14 08:43:00': 0, '2020-05-14 08:44:00': 0, '2020-05-14 08:45:00': 0, '2020-05-14 08:46:00': 0, '2020-05-14 08:47:00': 0, '2020-05-14 08:48:00': 0, '2020-05-14 08:49:00': 0, '2020-05-14 08:50:00': 0, '2020-05-14 08:51:00': 0, '2020-05-14 08:52:00': 0, '2020-05-14 08:53:00': 0, '2020-05-14 08:54:00': 0, '2020-05-14 08:55:00': 0, '2020-05-14 08:56:00': 0, '2020-05-14 08:57:00': 0, '2020-05-14 08:58:00': 1, '2020-05-14 08:59:00': 1, '2020-05-14 09:00:00': 0, '2020-05-14 09:01:00': 0, '2020-05-14 09:02:00': 0, '2020-05-14 09:03:00': 0, '2020-05-14 09:04:00': 0, '2020-05-14 09:05:00': 0, '2020-05-14 09:06:00': 0, '2020-05-14 09:07:00': 0, '2020-05-14 09:08:00': 0, '2020-05-14 09:09:00': 0, '2020-05-14 09:10:00': 0, '2020-05-14 09:11:00': 0, '2020-05-14 09:12:00': 0, '2020-05-14 09:13:00': 0, '2020-05-14 09:14:00': 0, '2020-05-14 09:15:00': 0, '2020-05-14 09:16:00': 0, '2020-05-14 09:17:00': 0, '2020-05-14 09:18:00': 0, '2020-05-14 09:19:00': 0, '2020-05-14 09:20:00': 0, '2020-05-14 09:21:00': 0, '2020-05-14 09:22:00': 0, '2020-05-14 09:23:00': 0, '2020-05-14 09:24:00': 0, '2020-05-14 09:25:00': 0, '2020-05-14 09:26:00': 0, '2020-05-14 09:27:00': 0, '2020-05-14 09:28:00': 0, '2020-05-14 09:29:00': 0, '2020-05-14 09:30:00': 0, '2020-05-14 09:31:00': -1, '2020-05-14 09:32:00': 0, '2020-05-14 09:33:00': 0, '2020-05-14 09:34:00': -1, '2020-05-14 09:35:00': 0, '2020-05-14 09:36:00': 0, '2020-05-14 09:37:00': 0, '2020-05-14 09:38:00': 0, '2020-05-14 09:39:00': 0, '2020-05-14 09:40:00': 0, '2020-05-14 09:41:00': 0, '2020-05-14 09:42:00': 0, '2020-05-14 09:43:00': 0, '2020-05-14 09:44:00': 0, '2020-05-14 09:45:00': 0, '2020-05-14 09:46:00': 0, '2020-05-14 09:47:00': 0, '2020-05-14 09:48:00': 0, '2020-05-14 09:49:00': 0, '2020-05-14 09:50:00': 0, '2020-05-14 09:51:00': 0, '2020-05-14 09:52:00': 0, '2020-05-14 09:53:00': 0, '2020-05-14 09:54:00': 0, '2020-05-14 09:55:00': 0, '2020-05-14 09:56:00': 0, '2020-05-14 09:57:00': 0, '2020-05-14 09:58:00': 0, '2020-05-14 09:59:00': 0, '2020-05-14 10:00:00': 0, '2020-05-14 10:01:00': 0, '2020-05-14 10:02:00': 0, '2020-05-14 10:03:00': 0, '2020-05-14 10:04:00': 0, '2020-05-14 10:05:00': 0, '2020-05-14 10:06:00': 0, '2020-05-14 10:07:00': 0, '2020-05-14 10:08:00': 1, '2020-05-14 10:09:00': 0, '2020-05-14 10:10:00': 0, '2020-05-14 10:11:00': 0, '2020-05-14 10:12:00': 0, '2020-05-14 10:13:00': 0, '2020-05-14 10:14:00': 0, '2020-05-14 10:15:00': 0, '2020-05-14 10:16:00': 0, '2020-05-14 10:17:00': 0, '2020-05-14 10:18:00': 0, '2020-05-14 10:19:00': 0, '2020-05-14 10:20:00': 0, '2020-05-14 10:21:00': 0, '2020-05-14 10:22:00': 0, '2020-05-14 10:23:00': 0, '2020-05-14 10:24:00': 0, '2020-05-14 10:25:00': 0, '2020-05-14 10:26:00': 0, '2020-05-14 10:27:00': 0, '2020-05-14 10:28:00': 0, '2020-05-14 10:29:00': 0, '2020-05-14 10:30:00': 0, '2020-05-14 10:31:00': -1, '2020-05-14 10:32:00': 0, '2020-05-14 10:33:00': 0, '2020-05-14 10:34:00': -1, '2020-05-14 10:35:00': 0, '2020-05-14 10:36:00': 0, '2020-05-14 10:37:00': 0, '2020-05-14 10:38:00': 0, '2020-05-14 10:39:00': 0, '2020-05-14 10:40:00': 0, '2020-05-14 10:41:00': 0, '2020-05-14 10:42:00': -1, '2020-05-14 10:43:00': 0, '2020-05-14 10:44:00': 0, '2020-05-14 10:45:00': 0, '2020-05-14 10:46:00': 0, '2020-05-14 10:47:00': 0, '2020-05-14 10:48:00': 1, '2020-05-14 10:49:00': 0, '2020-05-14 10:50:00': 0, '2020-05-14 10:51:00': 0, '2020-05-14 10:52:00': -1, '2020-05-14 10:53:00': 0, '2020-05-14 10:54:00': 0, '2020-05-14 10:55:00': 0, '2020-05-14 10:56:00': 1, '2020-05-14 10:57:00': 1, '2020-05-14 10:58:00': 1, '2020-05-14 10:59:00': 0, '2020-05-14 11:00:00': 0, '2020-05-14 11:01:00': 0, '2020-05-14 11:02:00': 0, '2020-05-14 11:03:00': 0, '2020-05-14 11:04:00': 0, '2020-05-14 11:05:00': 0, '2020-05-14 11:06:00': 0, '2020-05-14 11:07:00': 0, '2020-05-14 11:08:00': 1, '2020-05-14 11:09:00': 0, '2020-05-14 11:10:00': 0, '2020-05-14 11:11:00': 0, '2020-05-14 11:12:00': -1, '2020-05-14 11:13:00': 0, '2020-05-14 11:14:00': 0, '2020-05-14 11:15:00': 0, '2020-05-14 11:16:00': 0, '2020-05-14 11:17:00': 0, '2020-05-14 11:18:00': 1, '2020-05-14 11:19:00': 1, '2020-05-14 11:20:00': 0, '2020-05-14 11:21:00': 0, '2020-05-14 11:22:00': 1, '2020-05-14 11:23:00': -1, '2020-05-14 11:24:00': 0, '2020-05-14 11:25:00': 0, '2020-05-14 11:26:00': 0, '2020-05-14 11:27:00': 0, '2020-05-14 11:28:00': 0, '2020-05-14 11:29:00': 0, '2020-05-14 11:30:00': 1, '2020-05-14 11:31:00': 1, '2020-05-14 11:32:00': -1, '2020-05-14 11:33:00': 0, '2020-05-14 11:34:00': 0, '2020-05-14 11:35:00': 0, '2020-05-14 11:36:00': 1, '2020-05-14 11:37:00': 0, '2020-05-14 11:38:00': 0, '2020-05-14 11:39:00': 0, '2020-05-14 11:40:00': 0, '2020-05-14 11:41:00': -1, '2020-05-14 11:42:00': -1, '2020-05-14 11:43:00': 0, '2020-05-14 11:44:00': 0, '2020-05-14 11:45:00': 1, '2020-05-14 11:46:00': -1, '2020-05-14 11:47:00': 0, '2020-05-14 11:48:00': 1, '2020-05-14 11:49:00': 0, '2020-05-14 11:50:00': 0, '2020-05-14 11:51:00': -1, '2020-05-14 11:52:00': 0, '2020-05-14 11:53:00': 0, '2020-05-14 11:54:00': 0, '2020-05-14 11:55:00': 0, '2020-05-14 11:56:00': 0, '2020-05-14 11:57:00': 0, '2020-05-14 11:58:00': 0, '2020-05-14 11:59:00': 0, '2020-05-14 12:00:00': 0, '2020-05-14 12:01:00': 0, '2020-05-14 12:02:00': -1, '2020-05-14 12:03:00': 0, '2020-05-14 12:04:00': 0, '2020-05-14 12:05:00': 0, '2020-05-14 12:06:00': 0, '2020-05-14 12:07:00': 0, '2020-05-14 12:08:00': 0, '2020-05-14 12:09:00': 0, '2020-05-14 12:10:00': 0, '2020-05-14 12:11:00': 0, '2020-05-14 12:12:00': 0, '2020-05-14 12:13:00': 0, '2020-05-14 12:14:00': 1, '2020-05-14 12:15:00': 0, '2020-05-14 12:16:00': 0, '2020-05-14 12:17:00': 1, '2020-05-14 12:18:00': 0, '2020-05-14 12:19:00': 0, '2020-05-14 12:20:00': -1, '2020-05-14 12:21:00': 0, '2020-05-14 12:22:00': 0, '2020-05-14 12:23:00': 0, '2020-05-14 12:24:00': -1, '2020-05-14 12:25:00': 0, '2020-05-14 12:26:00': 0, '2020-05-14 12:27:00': 0, '2020-05-14 12:28:00': 0, '2020-05-14 12:29:00': 0, '2020-05-14 12:30:00': 0, '2020-05-14 12:31:00': 0, '2020-05-14 12:32:00': 0, '2020-05-14 12:33:00': 0, '2020-05-14 12:34:00': 0, '2020-05-14 12:35:00': 0, '2020-05-14 12:36:00': 0, '2020-05-14 12:37:00': 0, '2020-05-14 12:38:00': 0, '2020-05-14 12:39:00': 1, '2020-05-14 12:40:00': 0, '2020-05-14 12:41:00': 0, '2020-05-14 12:42:00': 0, '2020-05-14 12:43:00': 0, '2020-05-14 12:44:00': 0, '2020-05-14 12:45:00': 0, '2020-05-14 12:46:00': 0, '2020-05-14 12:47:00': 1, '2020-05-14 12:48:00': 0, '2020-05-14 12:49:00': 0, '2020-05-14 12:50:00': 0, '2020-05-14 12:51:00': 0, '2020-05-14 12:52:00': 1, '2020-05-14 12:53:00': 1, '2020-05-14 12:54:00': 0, '2020-05-14 12:55:00': 1, '2020-05-14 12:56:00': 0, '2020-05-14 12:57:00': 0, '2020-05-14 12:58:00': 0, '2020-05-14 12:59:00': 1, '2020-05-14 13:00:00': 0}


new_dates = []
new_dates_set = set([])
files_position = {}
for original_filename in sorted(dates):
	m_date = original_filename.replace(second=0, microsecond=0)
	if m_date not in new_dates_set:
		position = str(long_or_short[str(m_date)])
		files_position['crop_'+str(original_filename)+'.png'] = position
	new_dates_set.add(m_date)

#	
#	
	
#import tensorflow as tf
#print(tf.__version__)
#
#mnist = tf.keras.datasets.fashion_mnist
#
#(x_train, y_train), (x_test, y_test) = mnist.load_data()
#
#x_train, x_test = x_train.reshape(60000, 28, 28, 1), x_test.reshape(10000, 28, 28, 1)
#x_train, x_test = x_train / 255.0, x_test / 255.0
#
#model = tf.keras.models.Sequential([
#	tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
#	tf.keras.layers.MaxPooling2D(2, 2),
#	tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#	tf.keras.layers.MaxPooling2D(2, 2),
#	tf.keras.layers.Flatten(),
#	tf.keras.layers.Dense(256, activation=tf.nn.relu),
#	tf.keras.layers.Dense(10, activation=tf.nn.softmax)
#])
#
#print(model.summary())
#
#model.compile(optimizer='adam',
#							loss='sparse_categorical_crossentropy',
#							metrics=['accuracy'])
#
#model.fit(x_train, y_train, epochs=2)
#
#print(model.evaluate(x_test, y_test))


#import IPython.display as display
#from PIL import Image
#import numpy as np
#import matplotlib.pyplot as plt
#import os

for i,j in zip(files_position, os.listdir('./cropped')):
#	if files_position[i] == 0:
#		print('movie')
#		os.rename('./cropped/' + i, './nothing/' + i)
	try:
		if int(files_position[i]) ==  -1:
			os.rename('./cropped/' + i, './short/' + i)

		if int(files_position[i]) ==  0:
			os.rename('./cropped/' + i, './nothing/' + i)
		
		if int(files_position[i]) ==  1:
			os.rename('./cropped/' + i, './long/' + i)
	except:
		pass