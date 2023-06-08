const tutors = [
    {
        id: 1,
        firstName: 'Sophie',
        lastName: 'Klean',
        courses: ['Sciences', 'Physiology'],
        image: 'images/sophie.jpg',
    },
    {
        id: 2,
        firstName: 'Jennifer',
        lastName: 'Morgan',
        courses: ['English', 'Spanish'],
        image: 'images/single.jpg',
    },
    {
        id: 3,
        firstName: 'Rich',
        lastName: 'Klark',
        courses:['Business Admin', 'Product Management'],
        image: 'images/white2.png',
    },
    {
        id: 4,
        firstName: 'Kriz',
        lastName: 'Don',
        courses:['Product Design', 'Technical Writing'],
        image: 'images/tutor_1.png',
    },
    {
        id: 5,
        firstName: 'Rachel',
        lastName: 'Steve',
        courses:['Cloud Computation', 'Data Integration'],
        image: 'images/Test2.png',
    },
    {
        id: 6,
        firstName: 'Afolabi',
        lastName: 'Seyi',
        courses:['Data Analysis', 'Product Management'],
        image: 'images/teacher.jpg',
    }
    // Add more tutors...
];

const tutorsList = document.getElementById('tutors-list');

tutors.forEach(tutor => {
    const tutorCard = document.createElement('div');
    tutorCard.classList.add('tutor-card');

    const tutorImage = document.createElement('div');
    tutorImage.classList.add('tutor-image');

    const image = document.createElement('img');
    image.src = tutor.image;
    image.alt = `${tutor.firstName} ${tutor.lastName}`;

    tutorImage.appendChild(image);

    const tutorInfo = document.createElement('div');
    tutorInfo.classList.add('tutor-info');

    const name = document.createElement('h2');
    name.textContent = `${tutor.firstName} ${tutor.lastName}`;

    const courses = document.createElement('p');
    courses.textContent = `Courses: ${tutor.courses.join(', ')}`;

    tutorInfo.appendChild(name);
    tutorInfo.appendChild(courses);

    tutorCard.appendChild(tutorImage);
    tutorCard.appendChild(tutorInfo);

    tutorsList.appendChild(tutorCard);
});
