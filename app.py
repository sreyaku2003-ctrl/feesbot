"""
IVRM Pre-Admission Chatbot API - Complete Python Implementation
Academic Management System by VASPS
"""

from flask import Flask, request, jsonify , render_template
from flask_cors import CORS
from datetime import datetime
import re
import random
import os
import logging





app = Flask(__name__)
CORS(app)



#@app.route("/")
#def home():
    #return render_template("index.html")
    
if "__main__":

    @app.route("/")
    def home():
        return render_template("index.html")
    CORS(app)
# Comprehensive Knowledge Base for IVRM Pre-Admission Module
# Comprehensive Knowledge Base for IVRM Fees Portal
KNOWLEDGE_BASE = {
    # FEE ONLINE PAYMENT
    "Admission": {
        "keywords": [
            "admission", "online admisssion", "apply online", "how to apply",
            "payment process", "make payment", "pay online", "fee structure",
            "deadline", "admission date", "pay my fees"
        ],
        "responses": [
            """In the **Fee Online Payment** page, you can view and pay your fees:

**Left Side - Student Information:**
- Admission Number
- Student Name and Class
- Current Year Charges - Total fees for this academic year
- Current Year Outstanding - Pending fees (if any)

**Right Side - Fee Groups:**
Select the fee groups you want to pay:
- School Fees
- Bus Fees
- Hostel Fees
- Other Fees
- Book Fees

**How to Pay:**
1. Tick the checkbox of fee groups you want to pay
2. Click "Show" button
3. Review payment details
4. Select your payment method (Credit Card/Debit Card/Net Banking/UPI)
5. Complete payment

After payment, you'll see current paid fees and concession details.""",

            """To make a fee payment:

**Step 1:** Go to Transaction → Fee Online Payment
**Step 2:** Check your student information and outstanding amount on the left
**Step 3:** Select fee groups (tick checkboxes) - School/Bus/Hostel/Other/Book fees
**Step 4:** Click "Show" to see payment details
**Step 5:** Choose payment option and complete payment

You can see your current year charges, outstanding balance, paid fees, and any concessions on this page."""
        ]
    },

    # FEE GROUPS
    "feeGroups": {
        "keywords": [
            "fee groups", "types of fees", "school fees", "bus fees",
            "hostel fees", "book fees", "other fees", "fee categories",
            "what fees", "fee types"
        ],
        "responses": [
            """Fee Groups are different categories of fees:

**1. School Fees** - Tuition, exam fees, activities
**2. Bus Fees** - Transportation charges
**3. Hostel Fees** - Accommodation charges (if applicable)
**4. Other Fees** - Miscellaneous charges
**5. Book Fees** - Textbooks and materials

You can select multiple fee groups to pay together. Tick the checkboxes of the groups you want to pay, then click "Show" to see the payment details.""",

            """The fee portal has 5 main fee groups:

- **School Fees** - Main tuition and academic fees
- **Bus Fees** - Transport charges
- **Hostel Fees** - Boarding charges
- **Other Fees** - Extra activities, events
- **Book Fees** - Study materials

Select any combination by ticking checkboxes and click "Show" button to proceed with payment."""
        ]
    },

    # OUTSTANDING FEES
    "outstanding": {
        "keywords": [
            "outstanding", "pending fees", "due fees", "balance",
            "unpaid", "remaining fees", "how much pending",
            "check outstanding", "pending amount"
        ],
        "responses": [
            """**Current Year Outstanding** shows your pending fees for this academic year.

**Where to check:**
Go to Transaction → Fee Online Payment
- Left side shows "Current Year Outstanding"


**To clear outstanding:**
1. Select the fee groups with pending amounts
2. Tick the checkboxes
3. Click "Show" button
4. Make payment

You can also check detailed outstanding in **Std Fee Details** page for complete fee analysis.""",

            """Outstanding fees are displayed in the Fee Online Payment page on the left side under "Current Year Outstanding".

This shows the total pending amount you need to pay. To clear it:
- Tick the relevant fee group checkboxes
- Click "Show" to see breakdown
- Select payment method and pay

Check Std Fee Details page for complete fee analysis including term-wise outstanding."""
        ]
    },

    # PAYMENT METHODS
    "paymentMethods": {
        "keywords": [
            "payment method", "how to pay", "payment options",
            "credit card", "debit card", "net banking", "upi",
            "payment mode", "pay using", "payment gateway"
        ],
        "responses": [
            """Available payment methods in the Fee Portal:

**1. Credit Card** - Visa, Mastercard, Amex
**2. Debit Card** - All major banks
**3. Net Banking** - Online banking from your bank
**4. UPI** - Google Pay, PhonePe, Paytm, BHIM

**Payment Process:**
1. Select fee groups and click "Show"
2. Review payment details
3. Choose your preferred payment method
4. You'll be redirected to secure payment gateway
5. Complete payment
6. Receipt will be generated automatically

All payments are secure and encrypted.""",

            """You can pay fees using:

- **Credit/Debit Card** - Any bank
- **Net Banking** - Direct bank transfer
- **UPI** - PhonePe, Google Pay, Paytm, etc.

After selecting fee groups and clicking "Show", choose your payment method. The payment gateway is secure and PCI-DSS compliant. After successful payment, your receipt is auto-generated and can be downloaded from Portal Fee Receipt section."""
        ]
    },

    # PORTAL FEE RECEIPT
    "portalFeeReceipt": {
        "keywords": [
            "receipt", "fee receipt", "download receipt", "print receipt",
            "get receipt", "receipt copy", "payment receipt", "receipt number",
            "find receipt", "view receipt", "receipt download"
        ],
        "responses": [
            """**Portal Fee Receipt** - View and download all your payment receipts

**Location:** Transaction → Portal Fee Receipt

**How to access:**
1. Select Academic Year from dropdown (right side)
2. All receipts for that year will be displayed
3. Select the receipt number you want


**Options available:**
- **Print** - Print the receipt
- **Download** - Save as PDF to your device

Each receipt contains:
- Receipt number and date
- Student details
            """To download or print your fee receipt:

**Steps:**
1. Go to **Transaction → Portal Fee Receipt**
2. Select **Academic Year** from dropdown (right side)
3. Choose the **Receipt Number** from the list
4. Receipt will be displayed on screen
5. Click **Download** to save as PDF or **Print** to print

All receipts generated in that academic year will be available. Keep receipts safe for your records!"""
        ]
    },

    # RECEIPT DETAILS
    "receiptDetails": {
        "keywords": [
            "receipt details", "what's in receipt", "receipt information",  
            "receipt contains", "receipt format", "receipt has"
        ],
        "responses": [
            """Every fee receipt contains complete payment details:

**Student Information:**
- Admission Number
- Student Name
- Class and Section

**Payment Details:**
- Receipt Number (unique identifier)
- Receipt Date
- Academic Year
- Fee Groups paid (School/Bus/Hostel/Other/Book)

**Financial Information:**
- Amount Paid
- Payment Method used
- Transaction ID
- GST/Tax details (if applicable)
- Total Amount

**School Information:**
- School name and logo
- School address
- Contact details

Keep receipts safe for reference and records!"""
        ]
    },

    # STD FEE DETAILS
    "stdFeeDetails": {
        "keywords": [
            "fee details", "fee dashboard", "fee analysis", "overall fees",
            "fee summary", "complete fee", "total fees", "fee status",
            "fee overview", "std fee details", "student fee details"
        ],
        "responses": [
            """**Std Fee Details** is your complete fee dashboard!

**Location:** Transaction → Std Fee Details

This page shows **overall fee analysis** for the student including:

**1. Total Fee Structure**
- Annual fees breakdown
- Term-wise fees

**2. Payment Status**
- Total Fees Charged
- Total Paid
- Total Outstanding/Pending
- Concessions/Discounts applied

**3. Fee Group Analysis**
- School Fees status
- Bus Fees status
- Hostel Fees status
- Other Fees status
- Book Fees status

**4. Term-wise Breakdown**
- Term 1, Term 2, Term 3 fees
- Paid vs Pending for each term

**5. Payment History**
- All previous payments
- Receipt numbers
- Payment dates

This is your complete fee dashboard at a glance!""",

            """The **Std Fee Details** page is your fee dashboard showing:

**Overall Analysis:**
✅ Total annual fees
✅ Amount paid so far
✅ Outstanding balance
✅ Concessions received

**Detailed Breakdown:**
- Fee group-wise status (School, Bus, Hostel, Other, Book)
- Term-wise payments (Term 1, 2, 3)
- Payment history with dates and receipt numbers

**Visual Summary:**
- Charts showing paid vs pending
- Fee distribution across groups
- Monthly payment trends

Navigate to Transaction → Std Fee Details to see your complete fee analysis!"""
        ]
    },

    # CONCESSION
    "concession": {
        "keywords": [
            "concession", "discount", "fee waiver", "scholarship",
            "reduced fees", "fee reduction", "concession amount",
            "fee discount", "waiver"
        ],
        "responses": [
            """**Concession/Discount** information is displayed in Fee Online Payment page.

**Where to see:**
- Go to Transaction → Fee Online Payment
- Right side shows "Current Paid Fees" and "Concession"
- Concession amount is subtracted from your total fees

**Types of Concessions:**
- Merit-based scholarships
- Sibling discounts
- Financial assistance
- Early payment discounts
- Category-based fee waivers

**How it works:**
Total Fees - Concession = Amount You Pay

For detailed concession breakdown, check the Std Fee Details page which shows concessions applied to each fee group.""",

            """Concessions (discounts) are shown in the Fee Online Payment page on the right side.

**Your concession is automatically applied** and shows:
- Concession Amount
- Updated fee after discount

Common concessions:
- Sibling discount
- Merit scholarships
- Financial aid
- Early bird discounts

The final amount you pay already has the concession deducted. Check Std Fee Details for complete concession breakdown across all fee groups!"""
        ]
    },

    # CURRENT YEAR CHARGES
    "currentYearCharges": {
        "keywords": [
            "current charges", "this year fees", "annual fees",
            "total fees", "current year charges", "fee structure",
            "how much is fees", "annual charges"
        ],
        "responses": [
            """**Current Year Charges** show your total fees for this academic year.

**Where to find:**
Transaction → Fee Online Payment → Left side

This includes:
- School Fees (Tuition, activities, exams)
- Bus Fees (if opted)
- Hostel Fees (if opted)
- Book Fees
- Other Fees

**Formula:**
Current Year Charges = Total Annual Fees
Outstanding = Charges - Paid Amount

To see detailed breakdown of charges, select fee groups and click "Show" button, or check Std Fee Details page for complete analysis."""
        ]
    },

    # PAYMENT HISTORY
    "paymentHistory": {
        "keywords": [
            "payment history", "previous payments", "past payments",
            "payment records", "transaction history", "old payments",
            "paid before", "earlier payments"
        ],
        "responses": [
            """To view your **payment history:**

**Option 1: Portal Fee Receipt**
- Go to Transaction → Portal Fee Receipt
- Select Academic Year
- See all receipts from that year
- Click any receipt to view details

**Option 2: Std Fee Details**
- Go to Transaction → Std Fee Details
- Scroll to "Payment History" section
- See all payments with dates and receipt numbers

**Payment history shows:**
- Date of payment
- Receipt number
- Amount paid
- Fee groups paid
- Payment method used
- Transaction ID

Keep tracking your payments through these pages!"""
        ]
    },

    # TRANSACTION SECTION
    "transactionSection": {
        "keywords": [
            "transaction", "transaction section", "fee section",
            "where to pay", "fee pages", "transaction menu",
            "fee portal sections"
        ],
        "responses": [
            """The **Transaction** section has 3 main pages for fee management:

**1. Fee Online Payment** ⭐
- Make new fee payments
- View student info and outstanding
- Select fee groups to pay
- Choose payment method

**2. Portal Fee Receipt** 📄
- View all receipts
- Download/Print receipts
- Select by academic year
- Access receipt history

**3. Std Fee Details** 📊
- Complete fee dashboard
- Overall fee analysis
- Payment status summary
- Fee group breakdown
- Term-wise details

Navigate to Transaction menu to access all these pages!"""
        ]
    },

    # COMPLETE PROCESS
    "completeProcess": {
        "keywords": [
            "complete process", "full process", "step by step",
            "how it works", "payment procedure", "fee process",
            "payment flow", "complete guide"
        ],
        "responses": [
            """**Complete Fee Payment Process:**

**Step 1: Check Fees**
- Go to Transaction → Fee Online Payment
- See your Current Year Charges and Outstanding

**Step 2: Select Fee Groups**
- Tick checkboxes for groups you want to pay (School/Bus/Hostel/Other/Book)
- Click "Show" button

**Step 3: Review Payment Details**
- Check the amount breakdown
- Verify fee groups selected
- See any concessions applied

**Step 4: Make Payment**
- Choose payment method (Card/Net Banking/UPI)
- Complete secure payment

**Step 5: Get Receipt**
- Receipt auto-generated after payment
- Go to Portal Fee Receipt to download
- Print for your records

**Step 6: Track Status**
- Check Std Fee Details for updated status
- Monitor outstanding balance

**Tip:** Keep all receipts safe for future reference!""",

            """Here's your **complete fee journey:**

📝 **Check** → Go to Fee Online Payment, see charges and outstanding
✅ **Select** → Tick fee group checkboxes you want to pay
👀 **Review** → Click "Show" to see payment details
💳 **Pay** → Choose payment method and complete transaction
📄 **Receipt** → Download from Portal Fee Receipt
📊 **Track** → Monitor status in Std Fee Details

**Quick Tips:**
- You can pay multiple fee groups together
- Receipts are available immediately after payment
- Outstanding updates automatically after payment
- Check Std Fee Details for complete analysis
- All payments are secure and encrypted

Need help with any specific step?"""
        ]
    },

    # FAILED PAYMENT
    "failedPayment": {
        "keywords": [
            "payment failed", "failed transaction", "payment not successful",
            "payment error", "transaction failed", "payment declined",
            "money deducted", "payment pending"
        ],
        "responses": [
            """If your **payment failed or money was deducted:**

**Immediate Steps:**
1. Don't retry payment immediately
2. Wait 30 minutes for bank to process
3. Check your bank statement

**If money deducted but receipt not generated:**
- Amount will be auto-refunded within 5-7 working days
- OR
- Payment will be auto-reconciled within 24 hours
- Check Portal Fee Receipt after 24 hours

**If payment shows pending:**
- Wait 1-2 hours for confirmation
- Check bank SMS/email
- Contact school office if not resolved in 24 hours

**To verify:**
- Go to Std Fee Details
- Check if payment is reflected
- Look for receipt in Portal Fee Receipt

**Need help?**
Contact school accounts department with:
- Transaction ID
- Date and time of payment
- Amount
- Payment method used"""
        ]
    },

    # TERM-WISE FEES
    "termWiseFees": {
        "keywords": [
            "term fees", "term wise", "termwise fees", "term 1",
            "term 2", "term 3", "quarterly fees", "installment",
            "semester fees"
        ],
        "responses": [
            """**Term-wise Fee Information:**

Most schools divide annual fees into terms/quarters:

**Term 1** - April to July (25-30% of annual fees)
**Term 2** - August to November (25-30% of annual fees)
**Term 3** - December to March (40-50% of annual fees)

**Where to check:**
Go to **Std Fee Details** page
- See term-wise breakdown
- Check paid vs pending for each term
- View due dates for each term

**Payment:**
- You can pay any term's fees from Fee Online Payment
- Select relevant fee groups
- Make payment
- Outstanding automatically adjusts

**Note:** Some fee groups (like Bus Fees) may have monthly payments instead of term-wise."""
        ]
    },

    # LATE PAYMENT
    "latePayment": {
        "keywords": [
            "late payment", "late fees", "fine", "penalty",
            "overdue", "missed deadline", "payment deadline",
            "due date", "late fee charges"
        ],
        "responses": [
            """**Late Payment and Penalties:**

**Due Dates:**
- Check your fee schedule for term-wise due dates
- Usually displayed in Std Fee Details page
- Schools send reminders before due dates

**Late Payment Charges:**
- Late fees may be added if payment is overdue
- Amount varies by school policy
- Shows as "Other Fees" or separate charge

**To avoid late fees:**
- Set payment reminders
- Pay before term deadline
- Check outstanding regularly in Fee Online Payment

**If you have late fees:**
- It will appear in your Current Year Outstanding
- Select and pay along with regular fees
- Shows separately in receipt

**Financial difficulty?**
Contact school accounts department to discuss:
- Payment plan options
- Late fee waiver requests
- Installment arrangements"""
        ]
    }
}

import nltk

# Automatically download needed NLTK corpora if not already present
nltk.download('punkt')       # for word_tokenize
nltk.download('stopwords')   # for stopwords
nltk.download('wordnet')  
nltk.download('punkt_tab')
   # for lemmatization

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

"""
Enhanced ChatbotEngine with better context understanding
Replace the ChatbotEngine class in your code with this one
"""

class ChatbotEngine:
    """Intelligent chatbot with proper intent understanding and context-aware detection"""
    
    def __init__(self):
        self.knowledge_base = KNOWLEDGE_BASE
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
        # Pre-admission related vocabulary (expanded)
        self.domain_vocabulary = {
            'application', 'form', 'health', 'student', 'admission', 'school',
            'interview', 'test', 'oral', 'written', 'marks', 'score', 'exam',
            'registration', 'register', 'document', 'upload', 'photo', 'parent',
            'guardian', 'status', 'accepted', 'rejected', 'selected', 'confirmed',
            'schedule', 'date', 'time', 'venue', 'report', 'prospectus', 'enquiry',
            'fee', 'payment', 'transfer', 'class', 'year', 'academic', 'fill',
            'submit', 'complete', 'attend', 'check', 'verify', 'monitor','filled'
            'procedure', 'process', 'step', 'next', 'after', 'before', 'help',
            'guide', 'information', 'details', 'required', 'mandatory', 'medical',
            'chronic', 'disease', 'emergency', 'hospital', 'clinic', 'aadhaar',
            'email', 'mobile', 'address', 'birth', 'religion', 'caste', 'blood',
            'nationality', 'language', 'gender', 'age', 'filled', 'completed',
            'done', 'finished', 'submitted', 'what', 'how', 'when', 'where'
        }
        
        # Off-topic categories (only truly irrelevant topics)
        self.off_topic_categories = {
            'math_calculation': [r'\d+\s*[\+\-\*\/]\s*\d+'],  # Only pure math
            'weather': ['weather', 'temperature', 'rain', 'sunny', 'cloudy', 'forecast'],
            'entertainment': ['movie', 'film', 'song', 'music', 'game', 'actor', 'celebrity'],
            'food': ['recipe', 'cook', 'restaurant', 'dish', 'meal'],
            'sports': ['football', 'cricket', 'basketball', 'tennis', 'tournament'],
            'travel': ['vacation', 'hotel', 'flight', 'booking', 'tourist'],
            'shopping': ['amazon', 'flipkart', 'shopping', 'discount', 'sale'],
            'technology': ['phone', 'laptop', 'android', 'ios', 'windows'],
        }
        
        # Completion indicators (expanded)
        self.completion_indicators = {
            'filled', 'completed', 'done', 'finished', 'submitted',
            'attended', 'gave', 'took', 'got', 'received', 'have',
            'did', 'made', 'uploaded', 'registered'
        }
        
        # Next step indicators
        self.next_step_indicators = {
            'next', 'after', 'then', 'now', 'what now', 'proceed', 
            'following', 'afterward', 'subsequently'
        }
        
        # User state detection patterns (more flexible)
        # User state detection patterns (for fees portal)
        self.state_patterns = {
            'viewed_fees': [
                r'\b(viewed|checked|saw|seen).{0,20}(fees|charges|outstanding)\b',
                r'\b(fees|charges).{0,20}(viewed|checked|saw)\b'
            ],
            'selected_groups': [
                r'\b(selected|ticked|chose).{0,20}(fee group|groups|school fees|bus fees)\b',
                r'\b(fee group|groups).{0,20}(selected|ticked)\b'
            ],
            'payment_completed': [
                r'\b(paid|completed|made).{0,20}payment\b',
                r'\b(payment).{0,20}(done|completed|successful)\b',
                r'\bpayment.{0,10}successful\b'
            ],
            'receipt_downloaded': [
                r'\b(downloaded|got|received).{0,20}receipt\b',
                r'\breceipt.{0,20}(downloaded|saved)\b'
            ]
        }
                # Next step responses
        # Next step responses for fees portal
        self.next_steps = {
            'viewed_fees': """Great! Now that you've viewed your fees, here's what to do next:

        **Step 1: Select Fee Groups**
        Tick the checkboxes of fee groups you want to pay:
        - School Fees
        - Bus Fees
        - Hostel Fees
        - Other Fees
        - Book Fees

        **Step 2: Click "Show" Button**
        This will display the payment details

        **Step 3: Review Amount**
        Check the total amount and any concessions applied

        **Step 4: Make Payment**
        Choose your payment method and complete payment

        Need help with selecting fee groups?""",
            
            'selected_groups': """Perfect! After selecting fee groups and clicking "Show", here's next:

        **Review Payment Details:**
        - Check the amount breakdown
        - Verify fee groups selected
        - See any discounts/concessions

        **Choose Payment Method:**
        - RazorPay(Google Pay, PhonePe, etc.)
        - Easybuzz
        - Net banking

        **Complete Payment:**
        - You'll be redirected to secure payment gateway
        - Enter payment details
        - Confirm transaction

        **After Payment:**
        - Receipt generated automatically
        - Download from Portal Fee Receipt
        - Check updated balance in Std Fee Details

        Ready to proceed with payment?""",
            
            'payment_completed': """Excellent! Payment successful! Here's what to do next:

        **Immediate Next Steps:**

        1. **Download Receipt** 📄
        • Go to Transaction → Portal Fee Receipt
        • Select current Academic Year
        • Find your latest receipt
        • Click Download/Print

        2. **Verify Payment** ✅
        • Go to Std Fee Details
        • Check updated outstanding balance
        • Verify payment is reflected

        3. **Keep Records** 💾
        • Save receipt PDF
        • Print for your files
        • Note receipt number

        **Your payment has been recorded!**
        - Outstanding balance updated
        - Receipt available for download
        - Email confirmation sent (if provided)

        Would you like to know how to download your receipt?""",
            
            'receipt_downloaded': """Perfect! You have your receipt. Here's what you should know:

        **Receipt is Important For:**
        - Your records and reference
        - School admission/exam requirements
        - Proof of payment
        - Tax purposes (if applicable)

        **Next Actions:**

        1. **Keep Safe** 💾
        • Save PDF in organized folder
        • Print physical copy
        • Email to yourself for backup

        2. **Check Fee Status** 📊
        • Go to Std Fee Details
        • See remaining outstanding (if any)
        • Plan next payment

        3. **Future Payments** 💳
        • Set reminders for next term
        • Check due dates
        • Monitor outstanding regularly

        **All done for now!**
        Your fee payment is complete and recorded.

        Need help with anything else?"""
        }
        
        def extract_intent_and_entities(self, user_input):
            """Advanced NLP-based intent and entity extraction using semantic understanding"""
            input_lower = user_input.lower()
            tokens = word_tokenize(input_lower)
            
            # Remove stopwords and lemmatize for better understanding
            filtered_tokens = []
            for token in tokens:
                if token not in self.stop_words and token not in string.punctuation:
                    filtered_tokens.append(self.lemmatizer.lemmatize(token))
            
            # Advanced Intent Detection with Semantic Patterns
            intents = {
                'pay': {
                    'keywords': ['pay', 'payment', 'paying', 'paid', 'make payment', 'complete payment'],
                    'patterns': [
                        r'\b(pay|paying|make|complete).{0,10}(payment|fees?|amount)\b',
                        r'\bhow.{0,10}(do|can|to).{0,10}pay\b',
                        r'\bwant.{0,10}(to|).{0,10}pay\b'
                    ]
                },
                'locate': {
                    'keywords': ['where', 'which page', 'which section', 'find', 'locate', 'location'],
                    'patterns': [
                        r'\bwhere.{0,15}(is|can|do|to)\b',
                        r'\bwhich.{0,10}(page|section)\b',
                        r'\bhow.{0,10}(to|can).{0,10}(find|locate|access)\b'
                    ]
                },
                'check': {
                    'keywords': ['check', 'see', 'view', 'show', 'display', 'look'],
                    'patterns': [
                        r'\b(check|see|view|show|display).{0,15}(my|the|)\b',
                        r'\bhow.{0,10}(to|can).{0,10}(check|see|view)\b',
                        r'\bwhere.{0,10}(to|can).{0,10}(check|see)\b'
                    ]
                },
                'download': {
                    'keywords': ['download', 'get', 'obtain', 'save', 'print'],
                    'patterns': [
                        r'\b(download|get|obtain|print).{0,10}(receipt|invoice)\b',
                        r'\bhow.{0,10}(to|can).{0,10}(download|get|print)\b',
                        r'\bwant.{0,10}(receipt|invoice)\b'
                    ]
                },
                'understand': {
                    'keywords': ['what', 'explain', 'tell me', 'describe', 'meaning', 'means'],
                    'patterns': [
                        r'\bwhat\s+(is|are|does|means?)\b',
                        r'\b(explain|tell|describe).{0,10}(me|about|the)\b',
                        r'\bwhat.{0,10}(mean|meant)\b'
                    ]
                },
                'process': {
                    'keywords': ['how', 'steps', 'procedure', 'process', 'way', 'method'],
                    'patterns': [
                        r'\bhow\s+(to|do|can|should)\b',
                        r'\bwhat.{0,10}(steps|process|procedure)\b',
                        r'\b(steps|procedure|process|way).{0,10}(to|for)\b'
                    ]
                },
                'status': {
                    'keywords': ['status', 'balance', 'pending', 'outstanding', 'remaining'],
                    'patterns': [
                        r'\b(status|balance|pending|outstanding|remaining)\b',
                        r'\bhow\s+much.{0,10}(pending|due|balance|outstanding)\b',
                        r'\bwhat.{0,10}(is|my).{0,10}(status|balance|outstanding)\b'
                    ]
                },
                'failed': {
                    'keywords': ['failed', 'not working', 'error', 'problem', 'issue', 'declined'],
                    'patterns': [
                        r'\b(payment|transaction).{0,10}(failed|not.{0,5}working|error|problem)\b',
                        r'\b(failed|declined|rejected).{0,10}(payment|transaction)\b',
                        r'\bmoney.{0,10}deducted\b'
                    ]
                },
                'help': {
                    'keywords': ['help', 'assist', 'support', 'guidance', 'guide'],
                    'patterns': [
                        r'\b(help|assist|support|guide).{0,10}(me|with|)\b',
                        r'\bneed.{0,10}(help|assistance|guidance)\b'
                    ]
                }
            }
            
            # Detect intent using both keywords and patterns
            detected_intent = None
            max_confidence = 0
            
            for intent, data in intents.items():
                confidence = 0
                
                # Check keywords
                for keyword in data['keywords']:
                    if keyword in input_lower:
                        confidence += 2
                
                # Check patterns
                for pattern in data['patterns']:
                    if re.search(pattern, input_lower):
                        confidence += 3
                
                if confidence > max_confidence:
                    max_confidence = confidence
                    detected_intent = intent
            
            # Advanced Entity Detection with Context
            entities = {
                'fee_payment': {
                    'keywords': ['fee payment', 'online payment', 'pay fees', 'payment', 'paying fees'],
                    'context_words': ['pay', 'payment', 'fees']
                },
                'receipt': {
                    'keywords': ['receipt', 'invoice', 'proof', 'payment proof'],
                    'context_words': ['receipt', 'invoice', 'download', 'print']
                },
                'fee_groups': {
                    'keywords': ['fee groups', 'school fees', 'bus fees', 'hostel fees', 'book fees', 'other fees'],
                    'context_words': ['group', 'school', 'bus', 'hostel', 'book']
                },
                'outstanding': {
                    'keywords': ['outstanding', 'pending', 'due', 'balance', 'remaining', 'unpaid'],
                    'context_words': ['outstanding', 'pending', 'due', 'balance', 'owe']
                },
                'concession': {
                    'keywords': ['concession', 'discount', 'scholarship', 'waiver', 'reduced'],
                    'context_words': ['concession', 'discount', 'scholarship', 'waiver']
                },
                'payment_method': {
                    'keywords': ['payment method', 'credit card', 'debit card', 'upi', 'net banking', 'card'],
                    'context_words': ['card', 'upi', 'banking', 'method']
                },
                'fee_details': {
                    'keywords': ['fee details', 'fee dashboard', 'fee status', 'std fee details', 'complete details'],
                    'context_words': ['details', 'dashboard', 'summary', 'analysis']
                },
                'charges': {
                    'keywords': ['charges', 'annual fees', 'total fees', 'current charges', 'year charges'],
                    'context_words': ['charges', 'annual', 'total', 'current', 'year']
                },
                'term_fees': {
                    'keywords': ['term fees', 'term 1', 'term 2', 'term 3', 'quarterly', 'semester'],
                    'context_words': ['term', 'quarter', 'semester', 'installment']
                },
                'payment_history': {
                    'keywords': ['payment history', 'previous payments', 'past payments', 'transaction history'],
                    'context_words': ['history', 'previous', 'past', 'earlier', 'old']
                }
            }
            
            # Detect entities using semantic similarity
            detected_entities = []
            entity_confidence = {}
            
            for entity, data in entities.items():
                confidence = 0
                
                # Check direct keywords
                for keyword in data['keywords']:
                    if keyword in input_lower:
                        confidence += 3
                        break
                
                # Check context words in filtered tokens
                for context_word in data['context_words']:
                    lemmatized_context = self.lemmatizer.lemmatize(context_word)
                    if lemmatized_context in filtered_tokens:
                        confidence += 1
                
                if confidence > 0:
                    entity_confidence[entity] = confidence
            
            # Sort entities by confidence and select top ones
            if entity_confidence:
                sorted_entities = sorted(entity_confidence.items(), key=lambda x: x[1], reverse=True)
                detected_entities = [entity for entity, conf in sorted_entities if conf >= 2]
            
            # Context-aware entity disambiguation
            if not detected_entities and detected_intent:
                # Infer entities from intent
                intent_entity_map = {
                    'pay': ['fee_payment', 'fee_groups'],
                    'download': ['receipt'],
                    'check': ['outstanding', 'fee_details'],
                    'status': ['outstanding', 'fee_details']
                }
                if detected_intent in intent_entity_map:
                    detected_entities = intent_entity_map[detected_intent]
            
            
            
                return detected_intent, detected_entities
    
        def generate_contextual_response(self, intent, entities, user_input):
            """Generate intelligent response based on intent, entities, and semantic context"""
    
    # PAY intent - user wants to make payment
            if intent == 'pay':
                if 'fee_payment' in entities or 'fee_groups' in entities:
                    return self.knowledge_base['feeOnlinePayment']['responses'][0]
                elif 'outstanding' in entities:
                    return """To pay your outstanding fees:

**Step 1:** Go to Transaction → Fee Online Payment
**Step 2:** Check "Current Year Outstanding" on the left side
**Step 3:** Select fee groups with pending amounts (tick checkboxes)
**Step 4:** Click "Show" button to see payment details
**Step 5:** Choose payment method and complete payment

Your outstanding will be automatically updated after payment!"""
                elif any(group in user_input.lower() for group in ['school', 'bus', 'hostel', 'book', 'other']):
                    return self.knowledge_base['feeGroups']['responses'][0]
                else:
                    return self.knowledge_base['feeOnlinePayment']['responses'][1]
            
        # LOCATE intent - user asking "where"
            elif intent == 'locate':
                if 'receipt' in entities or 'receipt' in user_input.lower():
                    return self.knowledge_base['portalFeeReceipt']['responses'][0]
                elif 'fee_payment' in entities or 'pay' in user_input.lower():
                    return """Fee payment is in: **Transaction → Fee Online Payment**

Here you can:
- View your student information and current charges
- Check outstanding balance
- Select fee groups to pay
- Make online payment

Navigate to the Transaction section in the main menu!"""
                elif 'fee_details' in entities or 'dashboard' in user_input.lower():
                    return """Fee dashboard is in: **Transaction → Std Fee Details**

    This page shows:
    - Complete fee analysis
    - Payment status
    - Outstanding balance
    - Term-wise breakdown
    - Payment history

    Your complete fee overview in one place!"""
                elif 'outstanding' in entities:
                    return """Outstanding fees are shown in: **Transaction → Fee Online Payment**

    Check the left side for:
    - Current Year Charges
    - Current Year Outstanding (your pending amount)

    You can also see detailed outstanding in **Std Fee Details** page."""
                else:
                    return self.knowledge_base['transactionSection']['responses'][0]
    
    # CHECK intent - user wants to verify/view
            elif intent == 'check':
                        if 'outstanding' in entities or 'balance' in user_input.lower() or 'pending' in user_input.lower():
                            return self.knowledge_base['outstanding']['responses'][0]
                        elif 'fee_details' in entities or 'status' in user_input.lower():
                            return self.knowledge_base['stdFeeDetails']['responses'][0]
                        elif 'payment_history' in entities or 'history' in user_input.lower():
                            return self.knowledge_base['paymentHistory']['responses'][0]
                        elif 'charges' in entities or 'total' in user_input.lower():
                            return self.knowledge_base['currentYearCharges']['responses'][0]
                        elif 'concession' in entities or 'discount' in user_input.lower():
                            return self.knowledge_base['concession']['responses'][0]
                        else:
                            return self.knowledge_base['stdFeeDetails']['responses'][1]
                    
            # DOWNLOAD intent - user wants receipt
            elif intent == 'download':
                    if 'receipt' in entities or 'receipt' in user_input.lower():
                        return self.knowledge_base['portalFeeReceipt']['responses'][1]
                    else:
                        return self.knowledge_base['portalFeeReceipt']['responses'][0]
                
            # UNDERSTAND intent - user asking "what is"
            elif intent == 'understand':
                    if 'fee_groups' in entities or any(group in user_input.lower() for group in ['school fees', 'bus fees', 'hostel', 'book fees']):
                        return self.knowledge_base['feeGroups']['responses'][0]
                    elif 'concession' in entities or 'discount' in user_input.lower():
                        return self.knowledge_base['concession']['responses'][0]
                    elif 'outstanding' in entities:
                        return self.knowledge_base['outstanding']['responses'][0]
                    elif 'receipt' in entities:
                        return self.knowledge_base['receiptDetails']['responses'][0]
                    elif 'payment_method' in entities:
                        return self.knowledge_base['paymentMethods']['responses'][0]
                    elif 'term' in user_input.lower():
                        return self.knowledge_base['termWiseFees']['responses'][0]
                    elif 'fee_details' in entities or 'dashboard' in user_input.lower():
                        return self.knowledge_base['stdFeeDetails']['responses'][0]
                    else:
                        return self.knowledge_base['feeOnlinePayment']['responses'][0]
                
            # PROCESS intent - user asking "how to"
            elif intent == 'process':
                    if 'pay' in user_input.lower() or 'fee_payment' in entities:
                        return self.knowledge_base['completeProcess']['responses'][1]
                    elif 'receipt' in user_input.lower() or 'download' in user_input.lower():
                        return self.knowledge_base['portalFeeReceipt']['responses'][1]
                    elif 'check' in user_input.lower() and 'outstanding' in user_input.lower():
                        return self.knowledge_base['outstanding']['responses'][0]
                    else:
                        return self.knowledge_base['completeProcess']['responses'][0]
                
            # STATUS intent - user asking about status
            elif intent == 'status':
                if 'outstanding' in entities or 'balance' in user_input.lower():
                    return self.knowledge_base['outstanding']['responses'][0]
                elif 'payment' in user_input.lower():
                    return self.knowledge_base['stdFeeDetails']['responses'][1]
                else:
                    return self.knowledge_base['stdFeeDetails']['responses'][0]
            
            # FAILED intent - payment issues
            elif intent == 'failed':
                return self.knowledge_base['failedPayment']['responses'][0]
            
            # HELP intent - general help
            elif intent == 'help':
                return self.knowledge_base['transactionSection']['responses'][0]
            
            # If no specific match, try to infer from entities alone
            if entities:
                primary_entity = entities[0]
                entity_kb_map = {
                    'fee_payment': 'feeOnlinePayment',
                    'receipt': 'portalFeeReceipt',
                    'fee_groups': 'feeGroups',
                    'outstanding': 'outstanding',
                    'concession': 'concession',
                    'payment_method': 'paymentMethods',
                    'fee_details': 'stdFeeDetails',
                    'charges': 'currentYearCharges',
                    'term_fees': 'termWiseFees',
                    'payment_history': 'paymentHistory'
                }
                
                if primary_entity in entity_kb_map:
                    kb_key = entity_kb_map[primary_entity]
                    if kb_key in self.knowledge_base:
                        return self.knowledge_base[kb_key]['responses'][0]
            
            return None


    def is_off_topic(self, user_input):
        """Detect if query is truly off-topic (very strict now)"""
        input_lower = user_input.lower().strip()
                
                # Check for pure mathematical calculations
        if re.match(r'^\d+\s*[\+\-\*\/]\s*\d+\s*$', input_lower):
            return True
                
                # Check only for clearly off-topic keywords

        off_topic_keywords=["movie",'pre admission','game','cake','food','movie','football','amazon'
                            'hotel','vacation','laptop','film','song','cricket','sports','love','romance']
                
                # Count admission-related vs off-topic words
        admission_words = sum(1 for word in self.domain_vocabulary if word in input_lower)
        off_topic_words = sum(1 for word in off_topic_keywords if word in input_lower)
                
                # Only mark as off-topic if no admission words and has off-topic words
        if off_topic_words > 0 and admission_words == 0:
            return True
                
        return False


    def detect_user_state(self, user_input):
        """Detect what stage the user completed using regex patterns"""
        input_lower = user_input.lower()
                    
        for state, patterns in self.state_patterns.items():
            for pattern in patterns:
                if re.search(pattern, input_lower, re.IGNORECASE):
                    return state
                    
        return None


    def is_asking_next_step(self, user_input):
        """Check if user is asking about next steps"""
        input_lower = user_input.lower()
        
        # Direct next step questions
        next_patterns = [
            r'\bwhat.{0,10}next',
            r'\bnext.{0,10}step',
            r'\bwhat.{0,10}(after|now|then)',
            r'\bafter.{0,10}(this|that)',
            r'\bthen.{0,10}what',
            r'\bwhat.{0,10}should.{0,10}(i|we|do)',
            r'\bwhat.{0,10}to.{0,10}do',
            r'\bhow.{0,10}(to.{0,10})?proceed'
        ]
        return any(re.search(pattern, input_lower) for pattern in next_patterns)


    def detect_question_topic(self, user_input):
        """Advanced semantic topic detection using NLP"""
        input_lower = user_input.lower()
        tokens = word_tokenize(input_lower)
        filtered_tokens = [self.lemmatizer.lemmatize(t) for t in tokens if t not in self.stop_words]
        
        # Semantic topic patterns with priority
        topic_patterns = {
            'feeOnlinePayment': {
                'primary': [
                    r'\b(pay|make|complete).{0,15}(payment|fees?)\b',
                    r'\bhow.{0,10}(to|can|do).{0,10}pay\b',
                    r'\bonline\s+payment\b',
                    r'\bpay.{0,10}my.{0,10}fees?\b'
                ],
                'tokens': ['pay', 'payment', 'online', 'fee'],
                'weight': 3
            },
            'portalFeeReceipt': {
                'primary': [
                    r'\b(download|get|print|view).{0,10}(receipt|invoice)\b',
                    r'\breceipt\b',
                    r'\bwhere.{0,10}(to|can).{0,10}(download|get|find).{0,10}receipt\b'
                ],
                'tokens': ['receipt', 'download', 'print', 'invoice'],
                'weight': 3
            },
            'outstanding': {
                'primary': [
                    r'\b(outstanding|pending|due|balance|remaining)\b',
                    r'\bhow\s+much.{0,10}(pending|due|owe|outstanding)\b',
                    r'\bcheck.{0,10}(outstanding|balance|pending)\b'
                ],
                'tokens': ['outstanding', 'pending', 'due', 'balance', 'owe'],
                'weight': 3
            },
            'feeGroups': {
                'primary': [
                    r'\bfee\s+groups?\b',
                    r'\b(school|bus|hostel|book|other)\s+fees?\b',
                    r'\bwhat.{0,10}(are|is).{0,10}fee\s+groups?\b'
                ],
                'tokens': ['group', 'school', 'bus', 'hostel', 'book'],
                'weight': 2
            },
            'stdFeeDetails': {
                'primary': [
                    r'\bfee\s+(details|dashboard|status|summary|analysis)\b',
                    r'\bcomplete.{0,10}fee\b',
                    r'\boverall.{0,10}fee\b',
                    r'\bstd\s+fee\s+details\b'
                ],
                'tokens': ['detail', 'dashboard', 'summary', 'analysis', 'complete'],
                'weight': 2
            },
            'concession': {
                'primary': [
                    r'\b(concession|discount|scholarship|waiver)\b',
                    r'\breduced.{0,10}fee\b'
                ],
                'tokens': ['concession', 'discount', 'scholarship', 'waiver'],
                'weight': 2
            },
            'paymentMethods': {
                'primary': [
                    r'\bpayment\s+(method|option|mode)\b',
                    r'\b(credit|debit)\s+card\b',
                    r'\b(upi|net\s+banking)\b',
                    r'\bhow.{0,10}(to|can).{0,10}pay\b'
                ],
                'tokens': ['method', 'option', 'card', 'upi', 'banking'],
                'weight': 2
            },
            'currentYearCharges': {
                'primary': [
                    r'\bcurrent.{0,10}(year.{0,10})?charges?\b',
                    r'\btotal.{0,10}fees?\b',
                    r'\bannual.{0,10}fees?\b'
                ],
                'tokens': ['current', 'charge', 'total', 'annual'],
                'weight': 2
            },
            'termWiseFees': {
                'primary': [
                    r'\bterm.{0,10}(wise|1|2|3|fees?)\b',
                    r'\bquarterly.{0,10}fee\b',
                    r'\bsemester.{0,10}fee\b'
                ],
                'tokens': ['term', 'quarter', 'semester', 'installment'],
                'weight': 2
            },
            'paymentHistory': {
                'primary': [
                    r'\bpayment.{0,10}history\b',
                    r'\b(previous|past|earlier|old).{0,10}payment\b',
                    r'\btransaction.{0,10}history\b'
                ],
                'tokens': ['history', 'previous', 'past', 'transaction'],
                'weight': 2
            }
        }
        
        # Calculate topic scores
        topic_scores = {}
        
        for topic, patterns in topic_patterns.items():
            score = 0
            
            # Check primary patterns
            for pattern in patterns['primary']:
                if re.search(pattern, input_lower):
                    score += patterns['weight'] * 3
            
            # Check tokens
            for token in patterns['tokens']:
                lemmatized_token = self.lemmatizer.lemmatize(token)
                if lemmatized_token in filtered_tokens:
                    score += patterns['weight']
            
            if score > 0:
                topic_scores[topic] = score
        
        # Return topic with highest score
        if topic_scores:
            return max(topic_scores.items(), key=lambda x: x[1])[0]
        
        return None


    def find_best_response(self, user_input, conversation_history=None):
        """Main response logic with context awareness"""
        input_lower = user_input.lower().strip()
        
        # Quick exit for empty input
        if not input_lower:
            return {
                "response": "I didn't receive any message. How can I help you with the Fee portal?",
                "category": "empty",
                "confidence": 1.0
            }
        
        # Check off-topic (very strict now)
        if self.is_off_topic(user_input):
            return {
                "response": "I'm sorry, I can only assist with Fee portal related queries. Please ask me about the fee payment, Fee receipt , Pending fees , status checking, or any other fee portal related procedures.",
                "category": "off-topic",
                "confidence": 1.0
            }
        
        # Reformulate vague questions using context
        vague_patterns = ['about that', 'about this', 'about it', 'more info', 'details']
        if any(pattern in input_lower for pattern in vague_patterns):
            if conversation_history:
                # Get last bot response to understand context
                for msg in reversed(conversation_history[-3:]):
                    if msg.get('role') == 'assistant':
                        last_category = msg.get('category', '')
                        if last_category in self.knowledge_base:
                            responses = self.knowledge_base[last_category]['responses']
                            return {
                                "response": random.choice(responses),
                                "category": last_category,
                                "confidence": 0.95,
                                "intent": "continuation_from_context"
                            }
        
        # Greetings
        greetings = ['hi', 'hello', 'hey', 'greetings', 'good morning', 
                    'good afternoon', 'good evening', 'namaste']
        if any(input_lower == g or input_lower.startswith(g + ' ') for g in greetings):
            return {
                "response": "Hello! How can I help you with the fee portal today? You can ask me about fee payment, Fee receipt , Pending fees , status checking, or any other fee portal related procedures.",
                "category": "greeting",
                "confidence": 1.0
            }
        
        # Thank you
        if re.search(r'\b(thank|thanks|appreciate)\b', input_lower):
            return {
                "response": "You're welcome! Feel free to ask if you have any other questions about pre-admission. I'm here to help!",
                "category": "gratitude",
                "confidence": 1.0
            }
        
        # Goodbye
        if re.search(r'\b(bye|goodbye|see you|good night)\b', input_lower):
            return {
                "response": "Goodbye! Thats all about you fees portal. Feel free to return if you have more questions!",
                "category": "farewell",
                "confidence": 1.0
            }
        
        # PRIORITY 1: Check if user completed something AND asking next step
        detected_state = self.detect_user_state(user_input)
        is_next_question = self.is_asking_next_step(user_input)
        
        if detected_state and is_next_question:
            # User said "I filled X, what next?"
            if detected_state in self.next_steps:
                return {
                    "response": self.next_steps[detected_state],
                    "category": f"next-after-{detected_state}",
                    "confidence": 1.0,
                    "intent": "completion_with_next_question",
                    "user_state": detected_state
                }
        
        # PRIORITY 2: Check if just stating completion
        if detected_state and not is_next_question:
            # User just said "I filled the application"
            if detected_state in self.next_steps:
                return {
                    "response": self.next_steps[detected_state],
                    "category": f"completed-{detected_state}",
                    "confidence": 1.0,
                    "intent": "completion_stated",
                    "user_state": detected_state
                }
        
        # PRIORITY 3: Asking next step without stating what they completed
        if is_next_question and not detected_state:
            # Check conversation history for context
            if conversation_history:
                for msg in reversed(conversation_history[-5:]):
                    if msg.get('role') == 'user':
                        user_msg = msg.get('message', '')
                        # Check for state
                        hist_state = self.detect_user_state(user_msg)
                        if hist_state and hist_state in self.next_steps:
                            return {
                                "response": self.next_steps[hist_state],
                                "category": f"next-from-history-{hist_state}",
                                "confidence": 0.9,
                                "intent": "next_step_from_context",
                                "detected_state": hist_state
                            }
                        
                        try:
                            hist_intent, hist_entities = self.extract_intent_and_entities(user_msg)
                        except:
                            hist_intent, hist_entities = None, []
                        
                        if hist_entities:
                            # Map entity to next step
                            entity_to_state = {
                                'application_form': 'application_form',
                                'health_form': 'health_form',
                                'registration': 'registration',
                                'interview': 'interview_completed',
                                'marks': 'marks_received'
                            }
                            for entity in hist_entities:
                                if entity in entity_to_state:
                                    state = entity_to_state[entity]
                                    if state in self.next_steps:
                                        return {
                                            "response": f"Based on our conversation about {entity.replace('_', ' ')}, here's what's next:\n\n{self.next_steps[state]}",
                                            "category": f"next-from-entity-{entity}",
                                            "confidence": 0.85,
                                            "intent": "next_step_from_entity_context"
                                        }
            
            # No context found, ask for clarification
            return {
                "response": """To guide you on the next steps, could you tell me which stage you're at?

    Please say something like:
    - "I filled the application form"
    - "I completed the health form"
    - "I registered my details"
    - "I attended the interview"
    - "I got my test marks"

    What did you last complete?""",
                "category": "clarify-stage",
                "confidence": 1.0,
                "intent": "next_step_needs_context"
            }
        
        # PRIORITY 4: Advanced Semantic understanding - intent + entities + context
        try:
            intent, entities = self.extract_intent_and_entities(user_input)
        except Exception as e:
            intent, entities = None, []

        if intent or entities:
            contextual_response = self.generate_contextual_response(intent, entities, user_input)
            if contextual_response:
                entity_str = '-'.join(entities[:2]) if entities else 'none'
                return {
                    "response": contextual_response,
                    "category": f"{intent}-{entity_str}" if intent else entity_str,
                    "confidence": 1.0,
                    "intent": f"semantic_{intent}" if intent else "entity_based",
                    "entities": entities
                }

        # PRIORITY 5: Semantic topic detection (advanced pattern matching)
        topic = self.detect_question_topic(user_input)
        if topic and topic in self.knowledge_base:
            responses = self.knowledge_base[topic]["responses"]
            return {
                "response": random.choice(responses),
                "category": topic,
                "confidence": 0.9,
                "intent": "semantic_topic_detection"
            }
        
        # PRIORITY 6: Keyword matching fallback
        best_match = None
        max_score = 0

        for category, data in self.knowledge_base.items():
            score = 0
            for keyword in data["keywords"]:
                if keyword.lower() in input_lower:
                    # More weight for longer, more specific keywords
                    score += len(keyword.split()) * 2

            if score > max_score:
                max_score = score
                best_match = category

        if best_match and max_score > 0:
            responses = self.knowledge_base[best_match]["responses"]
            return {
                "response": random.choice(responses),
                "category": best_match,
                "confidence": max_score / 10,
                "intent": "keyword_match"
            }
        
        # FINAL FALLBACK
        return {
            "response": """I can help you with:

    - **Application Form** - How to fill student and parent details
    - **Health Form** - What medical information is needed
    - **Registration** - How to verify your details
    - **Interview Schedule** - Oral and Written test dates
    - **Marks Entry** - Where to check test scores
    - **Status Tracking** - Application and Admission status
    - **Complete Process** - Full step-by-step guide
    - **Reports** - Available reports and downloads
    - **Fees** - Payment information

    What would you like to know about? Or tell me what stage you've completed!""",
            "category": "help",
            "confidence": 0.5,
            "intent": "general_help"
        }


chatbot = ChatbotEngine()

    # ==================== API ROUTES ====================

@app.route('/api/health', methods=['GET'])
def health_check():
        """Health check endpoint"""
        return jsonify({
            "status": "active",
            "service": "IVRM Pre-Admission Chatbot",
            "version": "2.0.0",
            "technology": "Python Flask",
            "features": [
                "Application Form guidance",
                "Health Form instructions",
                "Registration & Document View",
                "Interview Scheduling (Oral & Written)",
                "Marks Entry information",
                "Status Tracking (Application & Admission)",
                "Transfer Student process",
                "Reports Module (5 types)",
                "Fees information"
            ],
            "timestamp": datetime.now().isoformat()
        })


@app.route('/api/chatbot/greeting', methods=['GET'])
def get_greeting():
        return jsonify({
            "message": "Hi! I'm your intelligent pre-admission assistant. Ask me anything about the admission process!",
            "suggested_questions": [
                "How will I know if my child is selected?",
                "What to do after attending the interview?",
                "Where can I check test marks?",
                "Where to pay the fees?",
                "Show me the complete admission process"
            ],
            "timestamp": datetime.now().isoformat()
        })


@app.route('/api/chatbot/message', methods=['POST'])
def process_message():
        """Main chat endpoint - process user message and return response"""
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                "error": "Message is required",
                "timestamp": datetime.now().isoformat()
            }), 400
        
        user_message = data.get('message', '')
        session_id = data.get('sessionId')
        user_id = data.get('userId')
        conversation_history = data.get('conversationHistory', [])
        
        # Get response from chatbot engine WITH CONTEXT
        result = chatbot.find_best_response(user_message, conversation_history)
        
        return jsonify({
            "user_message": user_message,
            "bot_response": result["response"],
            "category": result["category"],
            "confidence": result.get("confidence", 0),
            "matched_keywords": result.get("matched_keywords", []),
            "intent": result.get("intent"),
            "session_id": session_id,
            "user_id": user_id,
            "timestamp": datetime.now().isoformat()
        })


@app.route('/api/chatbot/topics', methods=['GET'])
def get_topics():
        """Get all available topics"""
        topics = []
        for key, data in KNOWLEDGE_BASE.items():
            topics.append({
                "id": key,
                "name": re.sub(r'([A-Z])', r' \1', key).strip().title(),
                "keywords": data["keywords"],
                "response_count": len(data["responses"])
            })
        
        return jsonify({
            "topics": topics,
            "count": len(topics),
            "timestamp": datetime.now().isoformat()
        })


@app.route('/api/chatbot/help/<topic>', methods=['GET'])
def get_topic_help(topic):
        """Get help for a specific topic"""
        if topic in KNOWLEDGE_BASE:
            return jsonify({
                "topic": topic,
                "responses": KNOWLEDGE_BASE[topic]["responses"],
                "keywords": KNOWLEDGE_BASE[topic]["keywords"],
                "timestamp": datetime.now().isoformat()
            })
        else:
            return jsonify({
                "error": "Topic not found",
                "available_topics": list(KNOWLEDGE_BASE.keys()),
                "timestamp": datetime.now().isoformat()
            }), 404


@app.route('/api/chatbot/process-flow', methods=['GET'])
def get_process_flow():
        """Get complete admission process flow"""
        return jsonify({
            "process_flow": [
                {
                    "step": 1,
                    "name": "Fill Application Form",
                    "description": "Complete student and parent details, upload photo and necessary documents."
                },
                {
                    "step": 2,
                    "name": "Fill Health Form",
                    "description": "Provide health details, chronic conditions, preferred hospital, and emergency contact. This is mandatory."
                },
                {
                    "step": 3,
                    "name": "Verify in Registration Page",
                    "description": "Review all entered information in the Registration page and correct any errors before final submission."
                },
                {
                    "step": 4,
                    "name": "Interview Scheduling",
                    "description": "School assigns Oral and Written test dates. Check Interview Schedule for date, time and venue."
                },
                {
                    "step": 5,
                    "name": "Attend Tests",
                    "description": "Attend Oral and Written tests as scheduled; bring necessary documents and admit card if provided."
                },
                {
                    "step": 6,
                    "name": "Marks Entry",
                    "description": "School uploads oral and written test marks in the Marks Entry section after evaluating tests."
                },
                {
                    "step": 7,
                    "name": "Monitor Application Status",
                    "description": "Track Application Status (Waiting / Rejected / Accepted) in the Preadmission Status page."
                },
                {
                    "step": 8,
                    "name": "Monitor Admission Status",
                    "description": "After acceptance, Admission Status shows In Progress → Selected → Confirmed."
                },
                {
                    "step": 9,
                    "name": "Transfer to Admission",
                    "description": "Once Confirmed, student appears in Transfer Pre Admission to Admission. Admin finalises enrollment."
                },
                {
                    "step": 10,
                    "name": "Reports & Documentation",
                    "description": "Generate/download necessary reports (Prospectus, Registration, Schedule, Enquiry, Student Count) and fee receipts."
                }
            ],
            "timestamp": datetime.now().isoformat()
        })


    # Health-check / root quick page (optional friendly text)
@app.route('/', methods=['GET'])
def root_page():
        return (
            "<h3>IVRM Pre-Admission Chatbot API</h3>"
            "<p>Use <code>/api/chatbot/message</code> POST to talk to the bot. "
            "See <code>/api/health</code> and <code>/api/chatbot/greeting</code>.</p>"
        )


@app.route("/api/chat", methods=["POST"])
def chat_api():
        data = request.json
        user_message = data.get("message", "")

        engine = ChatbotEngine()
        result = engine.detect_intent(user_message)

        if result:
            return jsonify({"response": result["response"]})

        # fallback: keyword-based search
        for key, item in KNOWLEDGE_BASE.items():
            if any(kw in user_message.lower() for kw in item["keywords"]):
                return jsonify({"response": random.choice(item["responses"])})

        return jsonify({"response": "I couldn't understand that. Can you rephrase?"})


if __name__ == "__main__":
        app.run(debug=True, port=5004)