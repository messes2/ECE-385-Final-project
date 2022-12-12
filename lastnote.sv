module noteenable(
	input Clk,
	inout wire [3:0] enable,
	inout wire [3:0] lastcase,
	inout wire fsmcontrol);

	initial
		begin
			enable=4'b0001;
			lastcase=4'bzzzz;
			fsmcontrol=1'b0;
		end
	always_ff @(negedge Clk)
				begin
					fsmcontrol <= 1'bz;
					enable<= 4'bzzzz;
					lastcase<= 4'bzzzz;
				end
endmodule
