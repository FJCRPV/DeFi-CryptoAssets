answers = {
    "name": "Francisco Perestrello",
    "student_id": "20241560",
    "a1":  "0xe4d238521b5195D58d021d0D35b36260b00ae70f", # wallet address
    "a2":  "0x135083c3e8ba7048b47ca65eba2d3fdab5db4f824eed3b2868f0190e6cceba8a", # transaction hash
    
    "a3":  "By providing liquidity to a pool on Uniswap V3, the source of yield are \
        the trading fees. Liquidity providers (LPs) earn a portion of said fees on each \
        swap that occurs within the price range they provide liquidity to as a reward for \
        enabling these trades. This design allows LPs to simulate active market-making \
        strategies and potentially generate higher returns on deposited capital. \
        The main technical risk is impermanent loss, which arises when the relative \
        price of the two provided assets diverges from the initial ratio at the \
        time of deposit. As a result, when the liquidity is withdrawn, the dollar \
        value of the assets might be less than if one had simply held them outside \
        the pool. In Uniswap V3, this is further influenced by concentrated liquidity: \
        if the market price moves outside the LPs specified range, the position \
        becomes inactive and stops earning fees, with the position fully converted \
        into the less valuable asset.", # free text answer to question 3
    
    "a4":  "0x7cb02b1938560e024c47adeea634afa577bded33b778c0472eb98df7f96f90ea", # transaction hash
    "a5":  "0x6f34268afd740e52da3bd47e1355d5ed25159f8febe5274257284a4cbc66b2e8", # transaction hash
    "a6":  "0x4bab51f7a3f3d0e1315dc44717c49ff1e5ed005fb9e18eb02c11570d238ef35c", # transaction hash

    "a7":  "Yes, I had to approve token spending before supplying WBTC to the \
        Aave protocol. This is a standard step in ERC-20 token interactions.\
        ERC-20 tokens, like WBTC, require an explicit approval from the user \
        before a smart contract can transfer tokens on their behalf. This is \
        a security measure to ensure that only trusted contracts can access the user’s tokens. \
        In this case, when supplying WBTC to Aave, the first transaction was an 'Approve' \
        transaction, allowing the protocol's smart contract to spend up to a certain amount \
        of WBTC from my wallet. The second transaction was the actual deposit, where Aave \
        transfered the approved amount of WBTC from my wallet into their lending pool.", # free text answer to question 7

    "a8":  "0xf2c26e8ff7f33ece26d9c95f657190cf13114230a67bd1a6515addcb28de8a20", # transaction hash
    "a9":  "0x8670746f2dad5034eccb87b4d2d32359e218a2a1f9c6b0cf4c371cb0eeff5ff0", # transaction hash
    "a10": "0xe0fb68e488d57bcf589656e1725cce454714b66452673d708c5165076079e5a1", # transaction hash
    "a11": "0x69c7d7044deefbc9f2c584e0ec232d29555b56f3661af8b2799ed906c4dd6eec", # transaction hash
    "a12": "0xe60a79428cd1bdbc905a0b2700e9105e969922f9651576d9411ade38e14dc1ed", # transaction hash

    "a13": "By supplying WBTC and borrowing additional EURS to buy even more WBTC, \
        I effectively created a leveraged long position on WBTC. This amplifies both \
        potential gains and losses. The main financial risk is that if WBTC decreases \
        in value, the value of my collateral drops while my debt remains the same, \
        causing the Loan-to-Value (LTV) ratio to rise. As DeFi lending protocols usually \
        require overcollateralization due to pseudo-anonimity, the Health Factor, \
        which reflects how safe the loan is, will decline as a result. If it falls \
        below 1, the position becomes vulnerable to liquidation, where Aave can sell \
        my collateral to repay part of the loan, possibly even incurring a penalty. \
        This exposes the strategy to significant liquidation risk due to market volatility.", # free text answer to question 13

    "a14": "0x85857e926e0ea5d1bde504b97f00a2fd8b86f680a2551a90c5e1e199253a1782", # transaction hash
    "a15": "0x3d62244d07497f65a82d27fb0e42779a8216c7d8393143921ad1ba9de4bce1e4", # transaction hash
}