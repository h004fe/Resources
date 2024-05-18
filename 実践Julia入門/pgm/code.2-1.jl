function disp(in,in_disp)
        io = IOBuffer();
        show(IOContext(io, :limit => true, :displaysize => (20, 40)), "text/plain", in);
        out = String(take!(io));
        #return out
        println("julia> $(rpl_in_disp)")
	println(out)
	println("")
end

rpl_in = 1
rpl_in_disp = rpl_in
disp(rpl_in, rpl_in_disp)

rpl_in = -12345
rpl_in_disp = rpl_in
disp(rpl_in, rpl_in_disp)

rpl_in = 1_000_000_000
rpl_in_disp = "1_000_000_000"
disp(rpl_in, rpl_in_disp)

exit()
