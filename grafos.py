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
        "HCCOR - Hospital do Câncer e do Coração": 32,
        "Hospital Universitário Antônio Pedro": 40,
        "Hospital Municipal Desembargador Leal Junior": 20
    },
    "HCCOR - Hospital do Câncer e do Coração": {
        "Hospital Universitário Antônio Pedro": 25,
        "Hospital Municipal Souza Aguiar": 38,
        "Hospital Municipal Desembargador Leal Junior": 18
    },
    "Hospital Universitário Antônio Pedro": {
        "Hospital Municipal Souza Aguiar": 12,
        "Hospital Municipal Ronaldo Gazolla": 30
    },
    "Hospital Municipal Souza Aguiar": {
        "Hospital Municipal Ronaldo Gazolla": 15,
        "Hospital Santa Teresa": 65
    },
    "Hospital Municipal Ronaldo Gazolla": {
        "Hospital Santa Teresa": 35
    },
    "Hospital Municipal Desembargador Leal Junior": {
        "Hospital Municipal de Magé": 25,
        "HCCOR - Hospital do Câncer e do Coração": 18
    },
    "Hospital Santa Teresa": {
        "Hospital Municipal Dr. Munir Rafful": 55,
        "Hospital Municipal Ronaldo Gazolla": 35
    },
    "Hospital Municipal de Magé": {
        "Hospital Municipal Dr. Munir Rafful": 80,
        "Hospital Municipal Desembargador Leal Junior": 35
    },
    "Hospital Municipal Dr. Munir Rafful": {}
}
