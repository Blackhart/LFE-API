class AccountType:
    """ Type d'un compte bancaire
    
    Il existe 3 types de comptes:
        - Compte Classique: qui sert à gérer son argent au quotidien et qui est désigné sous diverses appellations : compte courant, compte à vue, compte chèque, compte de dépôt
        - Compte d’Epargne: le compte épargne qui a l’avantage de produire des intérêts. On parle alors de comptes bancaires rémunérés. Dans cette catégorie, on trouve :
            - le compte d’épargne sur livret (Livret A, Livret Jeune, Livret de développement durable et solidaire – LDDS, Livret d’épargne populaire – LEP, etc.) ;
            - le compte pour le développement industriel (Codevi) ;
            - le plan d’épargne logement (PEL) et le compte épargne logement (CEL) ;
            - le plan d’épargne retraite (PERP) et le plan d’épargne pour la retraite collectif (Perco).
        - Compte Boursier: le compte-titres pour les produits d’investissement en bourse (achat de sicav, d’actions, d’obligations, etc.) et le plan d’épargne en actions (PEA)
    """
    STANDARD_ACCOUNT = 'STANDARD'
    SAVING_ACCOUT = 'SAVING'
    TRADING_ACCOUNT = 'TRADING'