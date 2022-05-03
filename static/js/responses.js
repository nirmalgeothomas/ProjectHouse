
function getBotResponse(input) {
    const greet=["hello","hi","hey","super","hey","good morning","good night"]
   
    const cas=["how are you","Are you okay","Is everything alright", "Are U" ]

    const b=["SEE YOU","BYE","bye", "see you","goodbye","GOODBYE" ]
   
    const p=["i need projects", "different types of projects", "Projects","computer science projects ","projects" ]

    const free=["is all the projects free", "is projects free", "free projects", "projects free", "free"]

    const download=["how to download the projects","how to download projects","how to download project", "how to download", "download projects", "download", "downloads", "download project"]
   
    const pay=["do we want to pay for projects", "pay for projects", "payment","do we need to pay", "do we want to pay for project"]

    const support=["will we get any support for doing the projects","will we get any support", "get any support in doing projects", "support"]
    
    const internship=["how to apply for intership","apply internship","apply for internship","internship"]

    const allprojects =["what are all the projects", "what are all projects", "all projects"]

    const howmany = ["how many projects are there","how many projects", "number of projects","total projects"]

    const platforms = ["how many platforms are there", "platforms"]

    const diffplatforms = ["what are the different platforms"]

    const modeinternship = ["whether the internship will be offine or online","internship mode", "mode of internship","internship types","is internship online or offline","online internship", "offline internship"]

    const certificates = ["do we get certificaates after completing internship","internship certificates","internship certificate","is there certificates for internships"]

    const python1=["python","Python","PYTHON","p","P"]
    const unity=['Unity', 'unity']
    const machine=["ML","ml","Machine","Machinelearning","MACHINE LEARNING","Machine learning","Machine Learning", "machine learning"]
    const java=["java","Java","JAVA"]
    const Android=["Android","android","ANDROID"]
    const php=["PHP","php"]
    if (greet.includes(input)){
        return "how can i help you";
    } else if (cas.includes(input)){
        return "I am Fine";
    } else if (free.includes(input)){
        return "All projects here have a fixed price";
    }else if (pay.includes(input)){
        return "yes, all projects have a fixed price";
    }else if (allprojects.includes(input)){
        return "we have number of projects in platforms like python, machine learning, java, Android, unity, .net, what kind of projects are you looking for, please type your platform in chatbox, eg:python ";
    }else if (certificates.includes(input)){
        return "yes, you will get internship certificate once you complete the internship successfully, visit this link to apply for internship.<a href=https://projecthouse.store/userintership>click here to apply</a>";
    }else if (modeinternship.includes(input)){
        return "we provide you both online and offline internship programs, according to your need you can select the mode of internships";
    }else if (platforms.includes(input)){
        return "we have 'six' different platforms,they are '1)machine learning 2)java 3)Unity 4)Android 5).net 6)python', what kind of projects are you looking for, please type your platform in chatbox, eg:python";
    }else if (diffplatforms.includes(input)){
        return "we have number of projects in different platforms like '1)machine learning 2)java 3)Unity 4)Android 5).net 6)python', what kind of projects are you looking for, please type your platform in chatbox, eg:python";
    }else if (howmany.includes(input)){
        return "many";
    }else if (internship.includes(input)){
        return "visit this link to apply for internship.<a href=https://projecthouse.store/userintership>click here to apply</a>";
    }else if (support.includes(input)){
        return "yes, we will be supporting you";
    }else if (download.includes(input)){
        return "choose your platform by clicking the link, eg: type 'python' in chatbox and click the link, view all the projects,there you can request to download the project";
    }else if (p.includes(input)) {
        return "what kind of project you are looking for?? 1)machine learning 2)java 3)Unity 4)Android 5).net 6)python";
    } else if (machine.includes(input)){
        // return "Intresting...ML projects that we provide are: 1) house price prediction \n 2) sms spam detection \n 3) language translation \n 4) academic performance prediction \n 5)stock price prediction \n 6) COVID-19 forecasting \n 7) age gender emotion\n8) air quality prediction \n9) automatic number plate recognition\n10) bigmart sales\n11) customer segmentation\n12) disease prediction\n13) driver drowsin\n14) loan prediction\n15) phishing website classification.....";
        return "<a href=https://projecthouse.store/userprojects/2>View available machine learning projects</a>  or <a href=https://projecthouse.store/view_ieee_papers/2>View available ML ieee papers</a>";
    }else if (java.includes(input)){
        // return "Intresting...Java projects that we provide are: 1) Online House Renting System \n 2) School Management System 3)Online Book Buying and Selling Portal 4)Towards Effective Bug Triage with Software Data Reduction Techniques 5)Extended AES with Custom Configurable Encryption 6)A BigData approach for classification and prediction of student result using MapReduce 7)Blood Bank Management System 8)Computer Inventory System 9)Data Security With Third Party Admin In Cloud Storage 10)Employee Pay Roll Management System....";
        return "<a href=https://projecthouse.store/userprojects/8>View available java projects</a>  or <a href=https://projecthouse.store/view_ieee_papers/8>View available java ieee papers</a>";
    }
    else if (Android.includes(input)){
        // return "Intresting...Android projects that we provide are: 1)Fake Caller Application 2)College Students Communication App 3)Timetable Manager 4)Food for Train App...";
        return "<a href=https://projecthouse.store/userprojects/6>View available android projects</a>  or <a href=https://projecthouse.store/view_ieee_papers/6>View available android ieee papers</a>";
    }else if (unity.includes(input)) {
        return "<a href=https://projecthouse.store/userprojects/3>View available unity projects</a>  or <a href=https://projecthouse.store/view_ieee_papers/3>View available unity ieee papers</a>";
    }
    else if (php.includes(input)){
        // return "Intresting...php projects that we provide are: 1)Paid Ads Website Application Synopsis 2)Online Lawyers Application Website Project Synopsis 3)Timetable Manager 4)Online Banking System 5)Job portal management system....";
        return "<a href=https://projecthouse.store/userprojects/9>View available php projects</a>  or <a href=https://projecthouse.store/view_ieee_papers/9>View available php ieee papers</a>";
    }
    
    
    else if (python1.includes(input)){
        // return "Intresting...Python projects that we provide are: 1) A Road Accident Prediction Model Using Data Mining Techniques \n 2) A Systematic Review of Predicting Elections Based on Social Media Data \n 3) Agricultural Crop Recommendations based on Productivity and Season \n 4) Design of medical image enhancement algorithm based on Python \n 5)Design of medical image enhancement algorithm based on Python \n 6) Handwritten Digit Recognition Using CNN \n 7) PCB Defect Detection USING OPENCV with Image Subtraction Method\n8) Tomato Leaf Disease Identification by Restructured Deep Residual Dense Network\n9)Blood cell counting using Python opencv....10)Novel Image Processing Technique for Feature Detection of Wheat Crops using Python OpenCV providing you the links to view python projects <a href=https://projecthouse.store/userprojects/1>View available python projects</a> ";
        return "<a href=https://projecthouse.store/userprojects/1>View available python projects</a> or <a href=https://projecthouse.store/view_ieee_papers/1>View available python ieee papers</a>"
    }
    else if (b.includes(input)) {
        return "good bye";
    }
    else {
        return "Sorry i didn't catch that.Can you try again?";
    }


    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}