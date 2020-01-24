fn main() {
	// Create input variable
	let my_input = "Pinewood";
	// Reverse the input using a 'rev' iterator
	let reversed_input: String = my_input.chars().rev().collect();
	// Print the reversed input
	println!("{}", reversed_input);
}