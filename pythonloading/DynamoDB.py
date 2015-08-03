import boto3


def handle_ivindex(data):
    # ivindex underlying_symbol,quote_datetime,iv30,iv60,iv90,iv120,iv180,iv360,iv720,expiry_iv1,expiry_iv2,expiry_iv3,expiry_iv4,expiry_iv5,expiry_iv6,expiry_iv7,expiry_iv8,expiry_iv9,expiry_iv10,expiry_iv1_date,expiry_iv2_date,expiry_iv3_date,expiry_iv4_date,expiry_iv5_date,expiry_iv6_date,expiry_iv7_date,expiry_iv8_date,expiry_iv9_date,expiry_iv10_date
    pass


def handle_calcs(data):
    client = boto3.resource('dynamodb')

    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'expiration_date',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'quoted_option_root',
                'AttributeType': 'S'
            }
        ],
        TableName='options-eod-calc',
        KeySchema=[
            {
                'AttributeName': 'quoted_option_root',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'expiration_date',
                'KeyType': 'RANGE'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 200,
            'WriteCapacityUnits': 10
        },
        StreamSpecification={
            'StreamEnabled': False
        }
    )
    # calcs underlying_symbol,quote_date,root,expiration,strike,option_type,open,high,low,close,trade_volume,bid_size_1545,bid_1545,ask_size_1545,ask_1545,underlying_bid_1545,underlying_ask_1545,implied_underlying_price_1545,active_underlying_price_1545,implied_volatility_1545,delta_1545,gamma_1545,theta_1545,vega_1545,rho_1545,bid_size_eod,bid_eod,ask_size_eod,ask_eod,underlying_bid_eod,underlying_ask_eod,vwap,open_interest,delivery_code
    pass


def handle_eod(data):
    # do not need to compute... in calcs
    # eod   underlying_symbol,quote_date,root,expiration,strike,option_type,open,high,low,close,trade_volume,bid_size_1545,bid_1545,ask_size_1545,ask_1545,underlying_bid_1545,underlying_ask_1545,bid_size_eod,bid_eod,ask_size_eod,ask_eod,underlying_bid_eod,underlying_ask_eod,vwap,open_interest,delivery_code
    pass


eods = boto3.client('dynamodb')

handle_ivindex(eods)
handle_calcs(eods)
handle_eod(eods)

# client = boto3.client('dynamodb')
