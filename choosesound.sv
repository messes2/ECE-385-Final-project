module choosesound(
					input Clk,
					input [7:0] keycod,
					input [31:0] dater1,
					input [31:0]dater2,
					input [31:0]dater3,
					input [31:0]dater4,
					input [31:0]dater5,
					input [31:0]dater6,
					input [31:0]dater7,
					input [31:0]dater8,
					output logic [31:0]dater);
					always_comb
					begin
					case (keycod)
					8'h61 : begin
								dater=dater1;
							  end
					        
					8'h64 : begin
								
								dater=dater2;
							  end
			
					8'h77 : begin

								dater=dater3;
							 end
							  
					8'h78 : begin
								dater=dater4;
							 end	
					8'h16 : begin

								dater=dater1;
							  end
					        
					8'h46 : begin
								
								dater=dater2;
							  end
							  
					8'h87 : begin
								dater=dater4;
							 end
					8'h65 : begin
								dater=dater5;
							  end
					8'h71 : begin
								dater=dater6;
							  end
					8'h63 : begin
								dater=dater7;
							  end
					8'h7A : begin
								dater=dater8;
							  end
					default: dater=32'b0;
			   endcase
end
endmodule