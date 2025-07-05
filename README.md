ქართულად:
სულხან კვერნაძის უნივერსიტეტის მართვის სისტემა


პროექტის აღწერა
პროექტი წარმოადგენს ფილმ „ჩაჭრილები“-დან ცნობილი „სულხან კვერნაძის უნივერსიტეტის“ მართვის სისტემის მოდელირებულ ვერსიას. პროგრამის ძირითადი მიზანია უნივერსიტეტის ლექტორების, სტუდენტებისა და კურსების მართვა. სისტემაში შესაძლებელია ახალი სტუდენტების, ლექტორების და კურსების დამატება, არსებული მონაცემების რედაქტირება ან წაშლა. ყველა მოქმედება ხორციელდება მარტივი და ინტუიციური ინტერფეისის საშუალებით.
გარდა ძირითადი ფუნქციონალისა, პროექტი აერთიანებს სახალისო ელემენტებს, როგორიცაა კურსდამთავრებულებისა და დამფუძნებლების ცალკე სექციები, რაც შექმნილია იუმორისტული სტილის შესატანად.

ბაზის სტრუქტურა ისეა აგებული, რომ კონკრეტული დეპარტამენტის ლექტორი ასწავლის მხოლოდ იმ საგნებს, რომლებიც შესაბამის დეპარტამენტს ეკუთვნის. ეს უზრუნველყოფს მართვის სისტემის ლოგიკურ სტრუქტურას და რეალურ სიტუაციასთან დაახლოებულ მუშაობას. სისტემა მარტივად გასაგებია როგორც ადმინისტრატორებისთვის, ასევე უნივერსიტეტის პერსონალის სხვა წევრებისთვის.

გამოყენების ინსტრუქცია
პროექტი Python-შია შესრულებული და აქვს გრაფიკული ინტერფეისი (GUI). გამოსაყენებლად საჭიროა Python-ის უახლესი ვერსია და საჭირო ბიბლიოთეკების დაყენება (PyQt5, ასევე sqlite3 მონაცემთა ბაზა, რომელზეც მუშაობს პროექტი).
აპლიკაციის გაშვების შემდეგ მომხმარებელს შეუძლია:

  1. იხილოს ლექტორების, სტუდენტებისა და კურსების სიები.

  2. დაამატოს ახალი ლექტორები, სტუდენტები ან კურსები.

  3. განახორციელოს არსებული ჩანაწერების რედაქტირება ან წაშლა.

  4. იხილოს კურსდამთავრებულები და დამფუძნებლები იუმორისტული ფორმატით.
     სისტემა ავტომატურად აახლებს მონაცემთა ბაზას და უზრუნველყოფს ყველა ცვლის სწორ სინქრონიზაციას.

გუნდის წევრების როლები
პროექტზე მუშაობდა ორი წევრი: დავით შენგელია და ვაჟა ცერცვაძე.

  1. დავით შენგელია პასუხისმგებელი იყო მონაცემთა ბაზების შექმნაზე და მათ შორის კავშირის სწორად აწყობაზე. ასევე მან UI ფაილები Python-ის კოდად გარდაქმნა და              განახორციელა ძირითადი ფუნქციონალი, მათ შორის CRUD ოპერაციები (დამატება, რედაქტირება, წაშლა).

  2. ვაჟა ცერცვაძე მუშაობდა პროექტის დიზაინზე, შექმნა პროგრამის ვიზუალური მხარე და უზრუნველყო სასიამოვნო და ლოგიკური ინტერფეისი. გარდა ამისა, ვაჟამ დაგეგმა          პროექტის ზოგადი სტრუქტურა, მოიფიქრა ფუნქციური ლოგიკა UI ელემენტების სწორად განლაგებისთვის და მონაწილეობდა ფუნქციური ნაწილის შემუშავებასა და                  ოპტიმიზაციაში.
  
  3. ორივე წევრმა ერთად იმუშავა კოდის საერთო სტრუქტურაზე, ლოგიკის შემოწმებასა და დებაგინგზე, რათა პროექტი გამართული და სრულფასოვანი გამოსულიყო.

მთლიანი პროექტისა და exe ფაილის სანახავად: https://drive.google.com/drive/folders/1e4bZNxR3_tfhEhyM9P_CZ3vItyEKL8zl?usp=sharing

English:
Sulkhan Kvernadze University Management System
Project Description
The project is a modeled version of the Sulkhan Kvernadze University Management System, inspired by the movie "Chachrilabi". The main goal of the application is to manage university lecturers, students, and courses. The system allows users to add new students, lecturers, and courses, as well as edit or delete existing records. All operations are carried out through a simple and intuitive graphical interface.

In addition to the core functionality, the project includes some humorous elements such as separate sections for graduates and founders, designed to bring a lighthearted style to the application.

The database structure is designed in a way that each lecturer from a specific department teaches only the courses that belong to that department. This ensures a logical system structure and a realistic approach. The system is easy to understand for both administrators and other university staff members.

Usage Instructions
The project is developed in Python and has a graphical user interface (GUI). To use the system, you will need the latest version of Python and the necessary libraries installed (such as PyQt5 and sqlite3 for the database).

After launching the application, the user can:

  1. View the lists of lecturers, students, and courses.
  
  2. Add new lecturers, students, or courses.
  
  3. Edit or delete existing records.
  
  4. View the graduates and founders sections, presented in a humorous format.
     The system automatically updates the database and ensures correct synchronization of all changes.

Team Member Roles
The project was developed by two team members: Davit Shengelia and Vazha Tsertsvadze.

  1. Davit Shengelia was responsible for creating the databases and setting up their correct interconnections. He also converted the UI files into Python code and       implemented the main functionality, including CRUD operations (Create, Read, Update, Delete).
  
  2. Vazha Tsertsvadze worked on the project design, created the application's visual elements, and ensured a pleasant and logical interface. Additionally, Vazha        planned the overall project structure, designed the functional logic for proper UI element placement, and contributed to developing and optimizing the              functional parts.
  
  3. Both team members worked together on the overall code structure, logic testing, and debugging to ensure the project was functional and complete.

To view the entire project and exe file: https://drive.google.com/drive/folders/1e4bZNxR3_tfhEhyM9P_CZ3vItyEKL8zl?usp=sharing
