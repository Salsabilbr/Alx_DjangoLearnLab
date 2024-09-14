/ Add event listener to login form  
document.querySelector('#login-form').addEventListener('submit', (e) => {  
  e.preventDefault();  
  const username = document.querySelector('#username').value;  
  const password = document.querySelector('#password').value;  
  // Send AJAX request to login view  
  fetch('/login/', {  
   method: 'POST',  
   headers: {  
    'Content-Type': 'application/json',  
   },  
   body: JSON.stringify({ username, password }),  
  })  
  .then((response) => response.json())  
  .then((data) => {  
   if (data.success) {  
    // Login successful, redirect to profile page  
    window.location.href = '/profile/';  
   } else {  
    // Login failed, display error message  
    document.querySelector('#login-error').innerHTML = data.error;  
   }  
  })  
  .catch((error) => console.error(error));  
});  
  
// Add event listener to register form  
document.querySelector('#register-form').addEventListener('submit', (e) => {  
  e.preventDefault();  
  const username = document.querySelector('#username').value;  
  const email = document.querySelector('#email').value;  
  const password1 = document.querySelector('#password1').value;  
  const password2 = document.querySelector('#password2').value;  
  // Send AJAX request to register view  
  fetch('/register/', {  
   method: 'POST',  
   headers: {  
    'Content-Type': 'application/json',  
   },  
   body: JSON.stringify({ username, email, password1, password2 }),  
  })  
  .then((response) => response.json())  
  .then((data) => {  
   if (data.success) {  
    // Registration successful, redirect to login page  
    window.location.href = '/login/';  
   } else {  
    // Registration failed, display error message  
    document.querySelector('#register-error').innerHTML = data.error;  
   }  
  })  
  .catch((error) => console.error(error));  
});
