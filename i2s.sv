
module i2s(
			  input sclk,
			  input lrclk,
			  input [31:0] i2s_Din,
			  output i2s_Dout
			 );
			 
			 
	logic [31:0] left;//left data
	logic [31:0] right;// right data;
	//logic [31:0] i2s_Din;
	
	always_ff @ (posedge sclk)
		begin
			if(lrclk) //enter left data and dump right data
				begin
					left <= i2s_Din;
					i2s_Dout <= right[31];
					right <= {right[30:0], 1'b0};
				end
		
			else //enter right data and dump left data
				begin
					right <= i2s_Din;
					i2s_Dout <= left[31];
					left <= {left[30:0], 1'b0};
				end
		end
 //audio audio_0 (.Data_In(4'b0), .ADDR_W(19'b0), .ADDR_R(ADDR_Count), .WE(1'b0), .Data_Out(i2s), .*);
endmodule
