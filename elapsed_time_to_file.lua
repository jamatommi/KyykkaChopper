-- "eplased_time_to_file.lua" -- VLC Extension script

-- [ Global variables ] --
def_hotkey=120 -- x key
end_hotkey=99  -- c key

--------------------------

function descriptor()
	return {
		title = "eps_time",
		version = "1.0",
		author = "valuex",
		url = "...",
		shortdesc = "save eplased time to file.",
		description = "save eplased time to file by hotkey"
	}
end
function activate()
    local item = vlc.input.item()
    local uri = item:uri()
    uri = string.gsub(uri, '^file:///', '')
	uri = vlc.strings.decode_uri(uri)
	uri = uri:gsub(".MP4", ".txt")
	uri = uri:gsub(".mp4", ".txt")

	filename = uri

	vlc.var.add_callback( vlc.object.libvlc(), "key-pressed", key_press)
end
function deactivate()
	vlc.var.del_callback( vlc.object.libvlc(), "key-pressed", key_press)
end
function close()
    vlc.deactivate()
end

function key_press( var, old, new, data)

	input = vlc.object.input()
	local curtime=vlc.var.get(input, "time")

	if new==def_hotkey then 
		prefix = ">"
		datafile=io.open(filename, "a")
		io.output(datafile)
		io.write(prefix .. curtime .. "\n")
		io.close()
	elseif new == end_hotkey then
		-- en jaksa koodata fiksusti.
		prefix = "<"
		datafile=io.open(filename, "a")
		io.output(datafile)
		io.write(prefix .. curtime .. "\n")
		io.close()
	end

end
