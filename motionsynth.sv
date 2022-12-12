//-------------------------------------------------------------------------
//                                                                       --
//                                                                       --
//      For use with ECE 385 Lab 62                                       --
//      UIUC ECE Department                                              --
//-------------------------------------------------------------------------


module motionsynth (

      ///////// Clocks /////////
      input     MAX10_CLK1_50, 

      ///////// KEY /////////
      input    [ 1: 0]   KEY,

      ///////// SW /////////
      input    [ 9: 0]   SW,

      ///////// LEDR /////////
      output   [ 9: 0]   LEDR,

      ///////// HEX /////////
      output   [ 7: 0]   HEX0,
      output   [ 7: 0]   HEX1,
      output   [ 7: 0]   HEX2,
      output   [ 7: 0]   HEX3,
      output   [ 7: 0]   HEX4,
      output   [ 7: 0]   HEX5,

      ///////// SDRAM /////////
      output             DRAM_CLK,
      output             DRAM_CKE,
      output   [12: 0]   DRAM_ADDR,
      output   [ 1: 0]   DRAM_BA,
      inout    [15: 0]   DRAM_DQ,
      output             DRAM_LDQM,
      output             DRAM_UDQM,
      output             DRAM_CS_N,
      output             DRAM_WE_N,
      output             DRAM_CAS_N,
      output             DRAM_RAS_N,

      ///////// VGA /////////
      output             VGA_HS,
      output             VGA_VS,
      output   [ 3: 0]   VGA_R,
      output   [ 3: 0]   VGA_G,
      output   [ 3: 0]   VGA_B,


      ///////// ARDUINO /////////
      inout    [15: 0]   ARDUINO_IO,
      inout              ARDUINO_RESET_N 

);
logic [23:0] hex_in;

always_comb begin
	LEDR[9] = jtag_R;
	LEDR[8] = jtag_A;
	jtag_Din = SW[7:0];
	jtag_WE = SW[9];
	jtag_Act = jtag_A;
end

jtag_controller jtag (
	.Clk(MAX10_CLK1_50),
	.Reset(Reset),
	.Act(jtag_Act),
	.WE(jtag_WE),
	.R(jtag_R),
	.A(jtag_A),
	.Din(jtag_Din),
	.Dout(jtag_Dout)
);

shift_reg shift_reg (
	.clk(MAX10_CLK1_50),
	.rst(Reset),
	.shift(jtag_R_pulse),
	.din(jtag_Dout),
	.dout(hex_in)
);

pulse r_pulse(
	.clk(MAX10_CLK1_50),
	.in(jtag_R),
	.out(jtag_R_pulse)
);

hex_driver hex_drivers [5:0] (
	.in  ({note,hex_in[15:0]}),//shows the keycode direction for debugging and shows the correct note
	.dp  ({1'b0, 1'b0, 1'b0, 1'b0, 1'b0, 1'b0}),
	.out ({HEX5, HEX4, HEX3, HEX2, HEX1, HEX0})
);

logic Reset_h, vssig, blank, sync, VGA_Clk;
logic [7:0] note;
notelight(.Clk(SCLK),.keycod(hex_in[7:0]), .keycod1(hex_in[15:8]), .noteled(note));
logic jtag_Act, jtag_WE;
logic jtag_R, jtag_A;
logic [7:0] jtag_Din;
logic [7:0] jtag_Dout;

logic jtag_R_pulse;
	
	vga_controller vga_ctrlr(.Clk(MAX10_CLK1_50), .Reset(Reset_h), .hs(VGA_HS), .vs(VGA_VS), .pixel_clk(VGA_Clk), .blank, .sync, .DrawX(drawxsig), .DrawY(drawysig));
	color_mapper clr_mpr(.BallX(ballxsig), .BallY(ballysig), .DrawX(drawxsig), .DrawY(drawysig), .Ball_size(ballsizesig), .Red, .Green, .Blue);
	ball b(.Reset(Reset_h), .frame_clk(VGA_VS), .keycod(hex_in[7:0]), .BallX(ballxsig), .BallY(ballysig), .BallS(ballsizesig));
//=======================================================
//  REG/WIRE declarations
//=======================================================
	logic SPI0_CS_N, SPI0_SCLK, SPI0_MISO, SPI0_MOSI, USB_GPX, USB_IRQ, USB_RST;
	logic [3:0] hex_num_4, hex_num_3, hex_num_1, hex_num_0; //4 bit input hex digits
	logic [1:0] signs;
	logic [1:0] hundreds;
	logic [9:0] drawxsig, drawysig, ballxsig, ballysig, ballsizesig;
	logic [7:0] Red, Blue, Green;
	logic [7:0] keycode;

//=======================================================
//  Structural coding
//=======================================================
	assign ARDUINO_IO[10] = SPI0_CS_N;
	assign ARDUINO_IO[13] = SPI0_SCLK;
	assign ARDUINO_IO[11] = SPI0_MOSI;
	assign ARDUINO_IO[12] = 1'bZ;
	assign SPI0_MISO = ARDUINO_IO[12];
	
	assign ARDUINO_IO[9] = 1'bZ; 
	assign USB_IRQ = ARDUINO_IO[9];
		
	//Assignments specific to Circuits At Home UHS_20
	assign ARDUINO_RESET_N = USB_RST;
	assign ARDUINO_IO[7] = USB_RST;//USB reset 
	assign ARDUINO_IO[8] = 1'bZ; //this is GPX (set to input)
	assign USB_GPX = 1'b0;//GPX is not needed for standard USB host - set to 0 to prevent interrupt
	
	//Assign uSD CS to '1' to prevent uSD card from interfering with USB Host (if uSD card is plugged in)
	assign ARDUINO_IO[6] = 1'b1;


	//Our A/D converter is only 12 bit
	//Final Project Declarations:
	logic i2c0_sda_in, i2c0_scl_in, i2c0_sda_oe, i2c0_scl_oe;
	logic [1:0] aud_mclk_ctr;
	logic [31:0] dater;
	wire [7:0] ramdater;
	logic [31:0] dater1;
	wire [7:0] ramdater1;
	logic [31:0] dater2;
	wire [7:0] ramdater2;
	logic [31:0] dater3;
	wire [7:0] ramdater3;
	logic [31:0] dater4;
	wire [7:0] ramdater4;
	logic [31:0] dater5;
	wire [7:0] ramdater5;
	logic [31:0] dater6;
	wire [7:0] ramdater6;
	logic [31:0] dater7;
	wire [7:0] ramdater7;
	logic [31:0] dater8;
	wire [7:0] ramdater8;
	logic [31:0] dater11;
	wire [7:0] ramdater11;
	logic [31:0] dater12;
	wire [7:0] ramdater12;
	logic [31:0] dater13;
	wire [7:0] ramdater13;
	logic [31:0] dater14;
	wire [7:0] ramdater14;
	logic [31:0] dater15;
	wire [7:0] ramdater15;
	logic [31:0] dater16;
	wire [7:0] ramdater16;
	logic [31:0] dater17;
	wire [7:0] ramdater17;
	logic [31:0] dater18;
	wire [7:0] ramdater18;
	logic SCLK, LRCLK, dout;
	wire f;
	wire [3:0] case; 
	wire [3:0] enable;
	g196 g3(.Clk(SCLK), .data_Out(ramdater18), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	a220 a3(.Clk(SCLK), .data_Out(ramdater17), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	b247 b3(.Clk(SCLK), .data_Out(ramdater16), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	c261 c4(.Clk(SCLK), .data_Out(ramdater15), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	d293 d4(.Clk(SCLK), .data_Out(ramdater14), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	e329 e4(.Clk(SCLK), .data_Out(ramdater13), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	f350 f4(.Clk(SCLK), .data_Out(ramdater12), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	g394 g4(.Clk(SCLK), .data_Out(ramdater11), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	a440 a4(.Clk(SCLK), .data_Out(ramdater1), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	b394 b4(.Clk(SCLK), .data_Out(ramdater2), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	c525 c5(.Clk(SCLK), .data_Out(ramdater3), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	d588 d5(.Clk(SCLK), .data_Out(ramdater4), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	e660 e5(.Clk(SCLK), .data_Out(ramdater5), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	f699 f5(.Clk(SCLK), .data_Out(ramdater6), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	g784 g5(.Clk(SCLK), .data_Out(ramdater7), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	a880 a5(.Clk(SCLK), .data_Out(ramdater8), .enable(enable), .enableout(lastcase), .fsmcontrol(f));
	
//=======================================================
//  Structural coding
//=======================================================
	//Final Project Structure:
	
	//Create 12.5 MHz clock using main clock
	assign ARDUINO_IO[3] = aud_mclk_ctr[1];
	//generate 12.5MHz CODEC mclk
	always_ff @(posedge MAX10_CLK1_50) begin
		aud_mclk_ctr <= aud_mclk_ctr + 1;
	end
	always_comb
		begin
		dater1={1'b0, ramdater1[7:0], 23'b0};
		dater2={1'b0, ramdater2[7:0], 23'b0};
		dater3={1'b0, ramdater3[7:0], 23'b0};
		dater4={1'b0, ramdater4[7:0], 23'b0};
		dater5={1'b0, ramdater5[7:0], 23'b0};
		dater6={1'b0, ramdater6[7:0], 23'b0};
		dater7={1'b0, ramdater7[7:0], 23'b0};
		dater8={1'b0, ramdater8[7:0], 23'b0};
		dater11={1'b0, ramdater11[7:0], 23'b0};
		dater12={1'b0, ramdater12[7:0], 23'b0};
		dater13={1'b0, ramdater13[7:0], 23'b0};
		dater14={1'b0, ramdater14[7:0], 23'b0};
		dater15={1'b0, ramdater15[7:0], 23'b0};
		dater16={1'b0, ramdater16[7:0], 23'b0};
		dater17={1'b0, ramdater17[7:0], 23'b0};
		dater18={1'b0, ramdater18[7:0], 23'b0};
		end
	//I2C Connections:
	assign i2c0_scl_in = ARDUINO_IO[15];
	assign ARDUINO_IO[15] = i2c0_scl_oe ? 1'b0 : 1'bz;
	assign i2c0_sda_in = ARDUINO_IO[14];
	assign ARDUINO_IO[14] = i2c0_sda_oe ? 1'b0 : 1'bz;
	assign SCLK=ARDUINO_IO[5];
	assign LRCLK=ARDUINO_IO[4];
	//Connect Line-In to Line-Out (delete later when create I2S)
	assign ARDUINO_IO[2] = dout;
	assign ARDUINO_IO[1] = dout;
	//assign ARDUINO_IO[1] = dout;
	i2s aaa (.sclk(SCLK), .lrclk(LRCLK), .i2s_Din(dater), .i2s_Dout(dout));
	choosesound1 pain (.Clk(SCLK), .keycod(hex_in[7:0]), .keycod1(hex_in[15:8]), .dater1(dater1), .dater2(dater2), .dater3(dater3), .dater4(dater4), .dater5(dater5), .dater6(dater6), .dater7(dater7), .dater8(dater8), .dater11(dater11), .dater12(dater12), .dater13(dater13), .dater14(dater14), .dater15(dater15), .dater16(dater16), .dater17(dater17), .dater18(dater18), .dater(dater));
	lab62soc u0 (
		.clk_clk                           (MAX10_CLK1_50),  //clk.clk
		.reset_reset_n                     (1'b1),           //reset.reset_n
		.altpll_0_locked_conduit_export    (),               //altpll_0_locked_conduit.export
		.altpll_0_phasedone_conduit_export (),               //altpll_0_phasedone_conduit.export
		.altpll_0_areset_conduit_export    (),               //altpll_0_areset_conduit.export
		.key_external_connection_export    (),            //key_external_connection.export
		//SDRAM
		.sdram_clk_clk(DRAM_CLK),                            //clk_sdram.clk
		.sdram_wire_addr(DRAM_ADDR),                         //sdram_wire.addr
		.sdram_wire_ba(DRAM_BA),                             //.ba
		.sdram_wire_cas_n(DRAM_CAS_N),                       //.cas_n
		.sdram_wire_cke(DRAM_CKE),                           //.cke
		.sdram_wire_cs_n(DRAM_CS_N),                         //.cs_n
		.sdram_wire_dq(DRAM_DQ),                             //.dq
		.sdram_wire_dqm({DRAM_UDQM,DRAM_LDQM}),              //.dqm
		.sdram_wire_ras_n(DRAM_RAS_N),                       //.ras_n
		.sdram_wire_we_n(DRAM_WE_N),                         //.we_n

		//USB SPI	
		.spi0_SS_n(SPI0_CS_N),
		.spi0_MOSI(SPI0_MOSI),
		.spi0_MISO(SPI0_MISO),
		.spi0_SCLK(SPI0_SCLK),
		
		//USB GPIO
		.usb_rst_export(USB_RST),
		.usb_irq_export(USB_IRQ),
		.usb_gpx_export(USB_GPX),
		
		//LEDs and HEX
		.hex_digits_export(),
		.led_wire_export(),
		.keycode_export(), 
		
		//VGA
		.i2c0_sda_in(i2c0_sda_in),
		.i2c0_scl_in(i2c0_scl_in),
		.i2c0_sda_oe(i2c0_sda_oe),
		.i2c0_scl_oe(i2c0_scl_oe)
		
	 );


//instantiate a vga_controller, ball, and color_mapper here with the ports.


endmodule
