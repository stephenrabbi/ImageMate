
// Function to handle the change event of the dropdown
function handleOptionChange() {
    var compressOption = document.getElementById("compressOption").value;
    if (compressOption === "compress") {
        // Set the API endpoint for compression
        apiUrl = "/compress";
        compress_val = compressOption
    } else if (compressOption === "decompress") {
        // Set the API endpoint for decompression
        apiUrl = "/decompress";
        compress_val = compressOption
    }

    return apiUrl
}

var ompress_val  

// Function to create and download the api result
function file_create(file_name, bytedata) {
    // Decode the base64 encoded string to binary data
    const base64String = atob(bytedata);
    const bytes = new Uint8Array(base64String.length);
  
    // Convert the binary data to a Uint8Array
    for (let i = 0; i < base64String.length; i++) {
      bytes[i] = base64String.charCodeAt(i);
    }
  
    // Create a Blob from the Uint8Array
    const blob = new Blob([bytes], { type: "application/octet-stream" });
  
    // Create a link element to initiate the file download
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = file_name;
    link.click();
  }
  


// Function to handle the change event of the file input
function handleFileChange() {
    var fileInput = document.getElementById("imageFile");
    var previewImage = document.getElementById("previewImage");
    // var downloadButton = document.getElementById("downloadButton");
    var submitButton = document.getElementById("submitButton");

    var file = fileInput.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
        previewImage.src = e.target.result;
        previewImage.style.display = "block";
        // downloadButton.disabled = true;  // Reset download button state
        submitButton.disabled = false;  // Enable submit button
    }

    reader.readAsDataURL(file);
}

// Function to handle the form submission
function handleSubmit(event) {
    event.preventDefault();

    var form = document.getElementById("imageUploadForm");
    var fileInput = document.getElementById("imageFile");
    var compressOption = document.getElementById("compressOption").value;

    if (fileInput.files && fileInput.files[0]) {
        var file = fileInput.files[0];
        var formData = new FormData();

        formData.append("image", file);
        formData.append("compressOption", compressOption);
        
        //get api url
        var apiUrl = handleOptionChange()

        // Make POST request to the API
        fetch(apiUrl, {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // API response handling
            var base64EncodedBytes = data.base64EncodedBytes;
            // console.log(base64EncodedBytes)


            // Generate download link and initiate download
            var downloadLink = document.createElement("a");
            downloadLink.href = "data:image/jpeg;base64," + base64EncodedBytes;
            downloadLink.download = `${compress_val}_image.jpg`;
            downloadLink.click();
        })
        .catch(error => console.error(error));
    }
}

// Add event listeners
document.getElementById("imageFile").addEventListener("change", handleFileChange);
document.getElementById("imageUploadForm").addEventListener("submit", handleSubmit);