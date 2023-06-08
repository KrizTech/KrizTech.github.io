const coursesData = [
    { name: 'Mathematics', students: 50 },
    { name: 'Physics', students: 35 },
    { name: 'English', students: 70 },
    { name: 'History', students: 45 },
    { name: 'Science', students: 60 },
    { name: 'Business', students: 55 },
    { name: 'HealthCare', students: 29 },
    { name: 'Data Analysis', students: 80 },
    // Add more courses...
];

// Calculate the total number of students
const totalStudents = coursesData.reduce((sum, course) => sum + course.students, 0);

// Create the chart
const chartContainer = document.getElementById('chart');

coursesData.forEach(course => {
    const courseElement = document.createElement('div');
    courseElement.className = 'bar';

    const courseName = document.createElement('div');
    courseName.className = 'course-name';
    courseName.textContent = course.name;

    const barFill = document.createElement('div');
    barFill.className = 'bar-fill';
    barFill.style.width = `${(course.students / totalStudents) * 100}%`;

    const barLabel = document.createElement('div');
    barLabel.className = 'bar-label';
    barLabel.textContent = `${course.students} students`;

    courseElement.appendChild(courseName);
    courseElement.appendChild(barFill);
    courseElement.appendChild(barLabel);

    chartContainer.appendChild(courseElement);
});
