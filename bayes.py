def bayes_inference(sensitivity, specificity, prevalence):
    P_Positive_Test_given_Drug_Use = sensitivity

    P_Positive_Test_given_No_Drug_Use = 1 - specificity

    P_Positive_Test = (P_Positive_Test_given_Drug_Use * prevalence) + \
                      (P_Positive_Test_given_No_Drug_Use * (1 - prevalence))

    P_Drug_Use_given_Positive_Test = (P_Positive_Test_given_Drug_Use * prevalence) / P_Positive_Test

    return P_Drug_Use_given_Positive_Test

try:
    sensitivity = float(input("Enter the sensitivity : "))
    specificity = float(input("Enter the specificity : "))
    prevalence = float(input("Enter the prevalence of drug use in the population : "))

    if not (0 <= sensitivity <= 1 and 0 <= specificity <= 1 and 0 <= prevalence <= 1):
        print("Please enter values between 0 and 1.")
    else:
        result = bayes_inference(sensitivity, specificity, prevalence)
        print(f"\nP(Drug Use | Positive Test): {result:.4f}")

except ValueError:
    print("Invalid input.")
