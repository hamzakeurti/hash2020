def evaluate_solution(D,A,libraries_list,books_val):
    signing_up = 0
    signed_up = {}
    score = 0
    scanned_books = []
    for d in range(D):
        # signing up process
        day_spent = False
        while (signing_up <= A) and (not day_spent):
            if libraries_list[signing_up]["signup"] = 0:
                signed_up[signing_up] = d
                signing_up += 1
                
                if signing_up > A:
                    break
            if libraries_list[signing_up]["signup"] > 0:
                libraries_list[signing_up]["signup"] -= 1
                day_spent = True
                
        
    # send books (=value)
    for l in signed_up:
        
        

def write_solution(solution,filename):
    with open(filename,"w") as f:
        f.write(solution)