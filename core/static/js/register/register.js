// const form = document.getElementById("form");
// const first_name = document.getElementById("id_first_name");
// const last_name = document.getElementById("id_last_name");
// const email = document.getElementById("id_email");
// const password_1 = document.getElementById("id_password1");
// const password_2 = document.getElementById("id_password2");


// //show input error
// function showError(input, message) {
//     const formControl = input.parentElement;
//     formControl.className = "form-control-register error";
//     const small = formControl.querySelector("small");
//     small.innerHTML = message
// }

// //show success outline
// function showSuccess(input) {
//     const formControl = input.parentElement;
//     formControl.className = "form-control-register success";
// }

// //is valid email
// function checkEmail(input){
//     const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//     if(re.test(input.value.trim())){
//         showSuccess(input)
//     }else{
//         showError(input,"Email not valid")
//     }
// }

// //password macth
// function checkPasswordMacth(input1, input2){
//     if(input1.value !== input2.value ){
//         showError(input2, "Password do not macth");
//     }
// }

// //check required
// function checkRequired(inputArr){
//     // inputArr.forEach(function(input){
//     //     if(input.value.trim() === ""){
//     //         showError(input, `${getFieldName(input)} is required`);
//     //     }else{
//     //         showSuccess(input);
//     //     }
//     // })
//     for (var i = 0; i < inputArr.length; i++) {
//         var input = inputArr[i];

//         if(input.value.trim() === ""){

//             showError(input, getFieldName(input)+" is required");
//         }else{

//             showSuccess(input);
//         }
//      }
// }

// //check length
// function checkLength(input, min, max){
//     if(input.value.length < min ){
//         showError(input, `${getFieldName(input)} must be at least ${min} characters`);
//     }else if(input.value.length > max){
//         showError(input, `${getFieldName(input)} must be at less than ${max} characters`);
//     }else{
//         showSuccess(input);
//     }
// }

// //get field name
// function getFieldName(field){

//     return field.name.charAt(0).toUpperCase() + field.name.slice(1);
// }

// //check first and lastname
// function checkFirstLastName(input){
// 	var letters = /^[A-Za-z]+$/;
// 	if(input.value.match(letters)){
//         showSuccess(input);
//     }else{
// 		showError(input, `${getFieldName(input)} must be letters only`);
//     }
// }

// //event listeners
// form.addEventListener("submit", function(e) {
//     checkRequired([first_name, last_name, email, password_1, password_2]);
// 	checkFirstLastName(first_name);
// 	checkFirstLastName(last_name);
//     checkLength(password_1,4, 25);
//     checkEmail(email);
//     checkPasswordMacth(password_1, password_2);
// });
