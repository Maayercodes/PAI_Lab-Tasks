from nltk.chat.util import Chat

pairs = [
    [r"(?i).*hello.*|.*hi.*|.*hey.*",
     ["Hello! How can I assist you with admissions?",
      "Hi there! Do you need admission information?",
      "Hey! Welcome to Superior University Admissions, how can I help?"]],

    [r"(?i).*programs.*offer.*|.*degree programs.*|.*courses available.*",
     ["We offer undergraduate, graduate, and PhD programs in various fields such as Engineering, Business, and Social Sciences."]],

    [r"(?i).*admission requirements.*|.*entry requirements.*|.*eligibility.*",
     ["You need academic transcripts, an entry test (if applicable), and other supporting documents."]],

    [r"(?i).*apply.*admission.*|.*admission process.*|.*steps to apply.*",
     ["Apply online through our official website or visit the admissions office for help."]],

    [r"(?i).*last date.*apply.*|.*admission deadline.*|.*when.*admission.*close.*",
     ["The admission deadline varies every semester. Please check the official website for the latest dates."]],

    [r"(?i).*scholarship.*|.*financial aid.*|.*tuition support.*",
     ["Yes, we offer merit-based and need-based scholarships. Check the scholarships section on our website."]],

    [r"(?i).*fee structure.*|.*tuition fees.*|.*cost of studying.*",
     ["The tuition fee depends on the program. Please refer to the fee section on our website."]],

    [r"(?i).*bye.*|.*goodbye.*|.*see you.*",
     ["Goodbye! Feel free to come back with more questions.",
      "Take care and good luck with your admission process!"]],
]

chatbot = Chat(pairs)

