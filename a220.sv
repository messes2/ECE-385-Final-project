module  a220
(
		input Clk,
		inout wire [3:0] enable,
		inout wire [3:0] enableout,
		inout wire [7:0] data_Out,
		inout wire fsmcontrol
);
logic [7:0] read_address;
logic [7:0] mem [200];
logic [31:0] loopcount;
initial
	begin
		$readmemh("soundhex/196g.hex", mem);
		loopcount=0;
	end

always_ff @ (posedge Clk)
	begin
				data_Out<= mem[read_address];//read 8bitwords
				read_address<=read_address+1;//go to next word
				if (read_address==200)//if on the last word, break
					begin
						read_address<=0;//reset loop
					end
			end
endmodule
