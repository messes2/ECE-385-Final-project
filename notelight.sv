module notelight(
					input Clk,
					input [7:0] keycod,
					input [7:0] keycod1,
					output [7:0] noteled);
					always_comb
					begin
					case (keycod1)
					8'h61 : begin
					case (keycod)
					8'h61 : begin
								noteled=8'hC4;
							  end
					        
					8'h64 : begin
								
								noteled=8'hB4;
							  end
			
					8'h77 : begin

								noteled=8'hC5;
							 end
							  
					8'h78 : begin
								noteled=8'hD5;
							 end	
					8'h65 : begin
								noteled=8'hE5;
							  end
					8'h71 : begin
								noteled=8'hF5;
							  end
					8'h63 : begin
								noteled=8'h95;
							  end
					8'h7A : begin
								noteled=8'hA5;
							  end
					default: noteled=8'h00;
			   endcase
				end
					8'h64 : begin
					case (keycod)
					8'h61 : begin
								noteled=8'h94;
							  end
					        
					8'h64 : begin
								
								noteled=8'hF4;
							  end
			
					8'h77 : begin

								noteled=8'hE4;
							 end
							  
					8'h78 : begin
								noteled=8'hD4;
							 end	
					        
					8'h65 : begin
								noteled=8'hC4;
							  end
					8'h71 : begin
								noteled=8'hB3;
							  end
					8'h63 : begin
								noteled=8'hA3;
							  end
					8'h7A : begin
								noteled=8'h93;
							  end
					default: noteled=8'h00;
			   endcase
				end 
				default: noteled=8'h00;
				endcase
				end
endmodule