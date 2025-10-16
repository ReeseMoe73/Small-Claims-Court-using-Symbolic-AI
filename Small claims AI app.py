from sklearn.naive_bayes import BernoulliNB

# Step 1: Define characteristics of various small claim type cases
# Feature format:
# [contains_deposit, money_not_refunded, contains_body_injury, contains_hospital, involves_negligence,
# involves_intention, contains_emotional_damage, contains_mental_damage, contains_money_owed,
# contains_home_damage, contains_landlord_tenant, involved_broken_contract ]
X = [
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # Security Deposit
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],  # Personal Injury
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # Debt Collection
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # Dispute with home contractor
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],  # Eviction
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # Contract Breach
]

# Step 2: Case labels (targets)
# 6=Security Deposit, 5 = Personal Injury, 4 = Debt Collection, 3 = Contract Dispute , 2 = Eviction, 1 = Contract Breach
y = [6, 5, 4, 3, 2, 1]

# Step 3: Train the Bernoulli Naive Bayes model
model = BernoulliNB()
model.fit(X, y)

# Step 4: Predict case type
case_type = [[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]]  # e.g., Personal Injury traits
prediction = model.predict(case_type)[0]

# Step 5: Output the predicted case type
cases = {
    1: "Contract Breach",
    2: "Eviction",
    3: "Contract Home Dispute",
    4: "Debt Collection",
    5: "Personal Injury",
    6: "Security Deposit"
}

print(f" This is the predicted court claim: {cases.get(prediction, 'Unknown')}")


# Define claim type knowledge base as rules and facts. Debt must under 5k, debt must be within 60 days, debt must be
# paid in fully, debt must have digitally signed agreement

class SmallClaimDebtCaseAISystem:
    def __init__(self, debt_amount, repayment_date, loan_paid, digital_signature):
        self.debt_amount = debt_amount
        self.repayment_date = repayment_date
        self.loan_paid = loan_paid
        self.digital_signature = digital_signature

# System retrieves some data from agreement page executed by plaintiff and defendent when digitally signed
# E.G Plaintiff loaned defendent $2000 to be returned in two months
    def amount_claim(self):
        return self.debt_amount == 2000

    def repayment_period(self):
        return self.repayment_date >= 60

    def was_loan_returned(self):
        return self.loan_paid ==  False

    def was_loan_signed(self):
        return self.digital_signature == True

    def assess_claim(self):
        # Inference Engine (symbolic rule chaining)
        if not self.amount_claim():
            return "Claim denied: Amount exceeds jurisdictional limit."

        if not self.repayment_period():
            return "Claim denied: Paid within time period."

        if not self.loan_paid:
            return "Claim denied: Receipt proves payment."

        if not self.digital_signature:
            return "Claim denied: Not digitally signed."

        return "Claim approved: Plaintiff is entitled to payment."

# Sample
case_1 = SmallClaimDebtCaseAISystem(debt_amount=2000, repayment_date =60, loan_paid=False, digital_signature=True)
result = case_1.assess_claim()
print(result)

case_2 = SmallClaimDebtCaseAISystem(debt_amount=2000, repayment_date =70, loan_paid=True, digital_signature=True)
result = case_2.assess_claim()
print(result)



