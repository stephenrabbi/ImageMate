# ImageMate
Image compressor

## Team
- Stephen Herbert - Software developer

## Technologies
- Django
- MongoDB
- Pillow
- Django REST Framework
- JavaScript
- HTML/CSS

## Why MongoDB?
Instead of using a traditional relational database like PostgreSQL, MongoDB was chosen as the database for ImageMate. MongoDB is a NoSQL database that is well-suited for handling large amounts of image data. Its flexible schema allows for storing images with varying dimensions and compression levels.

## Challenges
The main challenge addressed by the ImageMate project is optimizing image loading speed on websites. It provides image compression as a solution to improve site performance, resulting in faster load times and an enhanced user experience.

It's important to note that ImageMate cannot resolve issues related to slow internet connectivity or outdated devices that may affect image loading speeds on a website.

## Target Audience
The ImageMate project is aimed at website owners and developers seeking to enhance their site's performance by compressing images. The end users of these sites will benefit from faster load times and an improved browsing experience.

## Risks
There are both technical and non-technical risks associated with the ImageMate project:

- Technical risks include the possibility of the image compression algorithm not achieving the desired image quality. To mitigate this risk, extensive testing will be conducted using a variety of images to ensure consistent compression quality.

- Non-technical risks encompass unforeseen circumstances such as illness or personal emergencies that may cause delays. To mitigate such risks, clear communication among team members will be maintained, and contingency plans will be put in place to address any issues that may arise.

## Infrastructure
The project will follow the Git flow branching and merging strategy in the team's repository. This involves creating a development branch where all work is done and creating feature branches from the development branch. Once a feature is complete, it will be merged back into the development branch and then into the master branch for release.

The app will be deployed on a cloud-based platform such as Heroku. The deployment process will include creating a production-ready version of the app and uploading it to the platform.

A script will be used to populate the app with sample images for testing purposes.

Automated testing tools like PyTest will be utilized to ensure the proper functioning of the app.

## Existing Solutions
Similar existing solutions to ImageMate include TinyPNG, JPEGmini, and Kraken.io. These solutions also compress images to reduce file sizes.

ImageMate differentiates itself from these solutions by providing both API and site usage capabilities. Users will have the option to compress images directly on the site or integrate ImageMate's API into their own applications. Additionally, ImageMate utilizes a unique image compression algorithm tailored specifically to the project's requirements.

The decision to reimplement an existing solution was made with the belief that there is room for improvement in the current offerings. ImageMate's focus is on delivering a high-quality image compression algorithm with minimal loss in quality.

## Conclusion
ImageMate aims to optimize website performance by offering an image compression algorithm with API and site usage capabilities. By reducing image file sizes, it enables faster load times and enhances the user experience. Through careful implementation and testing, ImageMate seeks to provide a superior solution to existing image compression tools.
