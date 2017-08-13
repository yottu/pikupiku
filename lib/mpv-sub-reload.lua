seconds = 0
timer = mp.add_periodic_timer(1, function()
	mp.command('sub-reload')
    seconds = seconds + 1
end)
