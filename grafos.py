coordenadas = {
    "Hospital Municipal Dr. Ernesto Che Guevara": (-22.927806, -42.869156),
    "Hospital Universitário Antônio Pedro": (-22.894981, -43.112056),
    "Hospital Municipal Souza Aguiar": (-22.908177, -43.189647),
    "Hospital Municipal Ronaldo Gazolla": (-22.825811, -43.348071),
    "HCCOR - Hospital do Câncer e do Coração": (-22.823075, -42.977951),
    "Hospital Municipal Desembargador Leal Junior": (-22.737221, -42.848825),
    "Hospital Santa Teresa": (-22.507269, -43.193268),
    "Hospital Municipal Dr. Munir Rafful": (-22.499608, -44.123132),
    "Hospital Municipal de Magé": (-22.654184, -43.037339)
}

grafo = {
    "Hospital Municipal Dr. Ernesto Che Guevara": {
        "HCCOR - Hospital do Câncer e do Coração": 35,
        "Hospital Universitário Antônio Pedro": 45,
        "Hospital Municipal Desembargador Leal Junior": 30
    },
    "HCCOR - Hospital do Câncer e do Coração": {
        "Hospital Universitário Antônio Pedro": 30,
        "Hospital Municipal Souza Aguiar": 44,
        "Hospital Municipal Desembargador Leal Junior": 25
    },
    "Hospital Universitário Antônio Pedro": {
        "Hospital Municipal Souza Aguiar": 25,
        "Hospital Municipal Ronaldo Gazolla": 35
    },
    "Hospital Municipal Souza Aguiar": {
        "Hospital Municipal Ronaldo Gazolla": 40,
        "Hospital Santa Teresa": 70
    },
    "Hospital Municipal Ronaldo Gazolla": {
        "Hospital Santa Teresa": 60
    },
    "Hospital Municipal Desembargador Leal Junior": {
        "Hospital Municipal de Magé": 45,
        "HCCOR - Hospital do Câncer e do Coração": 25
    },
    "Hospital Santa Teresa": {
        "Hospital Municipal Dr. Munir Rafful": 130,
        "Hospital Municipal Ronaldo Gazolla": 55
    },
    "Hospital Municipal de Magé": {
        "Hospital Municipal Dr. Munir Rafful": 132,
        "Hospital Municipal Desembargador Leal Junior": 75
    },
    "Hospital Municipal Dr. Munir Rafful": {}
}
