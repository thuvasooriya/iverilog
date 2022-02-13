// Check that all parameters in a parameter port list after a `localparam` get
// elaborated as localparams, until the next `parameter`. Check that this is the
// case even when the data type of the parameter is redefined.

module a #(
  parameter A = 1, B = 2,
  localparam C = 3, real D = 4,
  parameter E = 5
);

initial begin
  if (A == 10 && B == 20 && C == 3 && D == 4 && E == 50) begin
    $display("PASSED");
  end else begin
    $display("FAILED");
  end
end

endmodule

module b;

  a #(
    .A(10),
    .B(20),
    .D(40), // This will cause an error
    .E(50)
  ) i_a();

endmodule
