# ============================================
# Quiz Game (Tuple Version)
# ============================================

# ============================================
# Quiz: C Programming, DSA, and Web Development
# ============================================

questions = (
    # C Programming
    "Which keyword is used to declare a constant variable in C?",
    "Which function is used to print output in C?",
    "What is the default return type of 'main()' in C if not specified?",
    "Which operator is used to access the value at a memory address?",
    "Which header file is required for 'printf()' function?",
    "Which loop will execute at least once regardless of condition?",
    "What is the size of 'int' in most 32-bit compilers?",
    "Which symbol is used to denote a single-line comment in C?",
    "What will 'sizeof(char)' return in C?",
    "What does 'break' statement do in a loop?",

    # DSA
    "Which data structure uses FIFO principle?",
    "Which data structure uses LIFO principle?",
    "What is the time complexity of binary search?",
    "Which traversal method visits left subtree, root, and then right subtree?",
    "Which algorithm is used to find the shortest path in a graph?",
    "Which sorting algorithm is considered the fastest on average for large datasets?",
    "In a linked list, what does the last node point to?",
    "Which data structure is used in function call stack?",
    "What is the worst-case time complexity of QuickSort?",
    "Which search technique checks each element one by one?",

    # Web Development
    "Which HTML tag is used to create a hyperlink?",
    "Which CSS property is used to change text color?",
    "Which HTML tag is used to display an image?",
    "What does CSS stand for?",
    "Which JavaScript method is used to select an element by ID?",
    "Which protocol is used to send webpages over the internet?",
    "In HTML, which tag is used to create an unordered list?",
    "Which JavaScript keyword is used to declare a variable that cannot be reassigned?",
    "Which CSS property controls the size of text?",
    "Which HTML tag is used to create a table row?"
)

options = (
    # C Programming
    ("A. const", "B. constant", "C. static", "D. immut"),
    ("A. scanf", "B. print", "C. printf", "D. cout"),
    ("A. void", "B. int", "C. float", "D. undefined"),
    ("A. *", "B. &", "C. ->", "D. %"),
    ("A. stdio.h", "B. conio.h", "C. iostream", "D. stdlib.h"),
    ("A. for loop", "B. while loop", "C. do-while loop", "D. infinite loop"),
    ("A. 2 bytes", "B. 4 bytes", "C. 8 bytes", "D. depends on compiler"),
    ("A. /* comment */", "B. // comment", "C. <!-- comment -->", "D. # comment"),
    ("A. 0", "B. 1", "C. 2", "D. depends on system"),
    ("A. Terminates the loop", "B. Skips current iteration", "C. Restarts loop", "D. Ends program"),

    # DSA
    ("A. Stack", "B. Queue", "C. Linked List", "D. Tree"),
    ("A. Stack", "B. Queue", "C. Array", "D. Graph"),
    ("A. O(n)", "B. O(log n)", "C. O(n log n)", "D. O(1)"),
    ("A. In-order", "B. Pre-order", "C. Post-order", "D. Level-order"),
    ("A. DFS", "B. BFS", "C. Dijkstra's Algorithm", "D. Prim's Algorithm"),
    ("A. Bubble Sort", "B. Quick Sort", "C. Insertion Sort", "D. Selection Sort"),
    ("A. NULL", "B. Head", "C. Tail", "D. First node"),
    ("A. Queue", "B. Array", "C. Stack", "D. Linked List"),
    ("A. O(n)", "B. O(n log n)", "C. O(n^2)", "D. O(log n)"),
    ("A. Binary Search", "B. Jump Search", "C. Linear Search", "D. Hash Search"),

    # Web Development
    ("A. <a>", "B. <link>", "C. <href>", "D. <url>"),
    ("A. font-color", "B. text-color", "C. color", "D. fgcolor"),
    ("A. <img>", "B. <image>", "C. <picture>", "D. <src>"),
    ("A. Creative Style Sheets", "B. Cascading Style Sheets", "C. Computer Style Sheets", "D. Colorful Style Sheets"),
    ("A. getElementById()", "B. querySelector()", "C. getByID()", "D. selectById()"),
    ("A. FTP", "B. HTTP", "C. SMTP", "D. TCP"),
    ("A. <ol>", "B. <ul>", "C. <li>", "D. <list>"),
    ("A. let", "B. const", "C. var", "D. final"),
    ("A. font-size", "B. text-size", "C. size", "D. font-height"),
    ("A. <td>", "B. <tr>", "C. <table>", "D. <th>")
)

answers = (
    # C Programming
    "A", "C", "B", "A", "A", "C", "B", "B", "B", "A",
    # DSA
    "B", "A", "B", "A", "C", "B", "A", "C", "B", "C",
    # Web Development
    "A", "C", "A", "B", "A", "B", "B", "B", "A", "B"
)


guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("✅ Correct!")
    else:
        print("❌ Incorrect!")
        print(f"The correct answer was: {answers[question_num]}")
    question_num += 1

# Results
print("\n---------------------------")
print("          RESULT           ")
print("---------------------------")

print("Answers: ", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

print("Guesses: ", end=" ")
for gue in guesses:
    print(gue, end=" ")
print()

score_percentage = int(score / len(questions) * 100)
print(f"\nYour score is: {score_percentage}%")
