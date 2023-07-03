function generatePassword(length) {
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+~`|}{[]:;?><,./-=";
  let password = "";

  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    password += characters.charAt(randomIndex);
  }

  return password;
}

// Prompt the user to enter the password length
const length = parseInt(prompt("Enter the length of the password:"));

// Generate the password
const password = generatePassword(length);

// Display the password
console.log(`Generated Password: ${password}`);

