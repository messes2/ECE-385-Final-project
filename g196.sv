module  g196
(
		input Clk,
		inout wire [3:0] enable,
		inout wire [3:0] enableout,
		inout wire [7:0] data_Out,
		inout wire fsmcontrol
);
logic [7:0] read_address;
// mem has width of 3 bits and a total of 400 addresses
logic [7:0] mem [224];
logic [31:0] loopcount;
initial
	begin
		$readmemh("soundhex/196g.hex", mem);
		loopcount=0;
	end

always_ff @ (posedge Clk)
	begin
//	if (we)
//		mem[write_address] <= data_In;
				data_Out<= mem[read_address];//read 8bitwords
				read_address<=read_address+1;//go to next word
				if (read_address==225)//if on the last word, break
					begin
						read_address<=0;//reset loop
					end
			end
endmodule