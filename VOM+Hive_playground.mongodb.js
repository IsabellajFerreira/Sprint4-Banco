/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
// Selecionando o database a ser utilizado
use('VOM+HIVE');


// Coleção de Produtos
db.produto.insertMany([ 
  {
    id_produto: 1,   
    nome: "Laptop",
    publico_alvo: "Entusiastas de Tecnologia",
    diferencial: "Alta qualidade",
    preco: 999.99,
    canal_vendas: "Online",
    categoria: "Eletronicos",
    descricao: "Produto eletronico de alta tecnologia",
    estoque: 50,
    avaliacao: 4.8,
    data_lancamento: new Date("2024-01-15")
  },
  {
    id_produto: 2,
    nome: "Smartphone",
    publico_alvo: "Entusiastas de Tecnologia",
    diferencial: "Baixo custo",
    preco: 699.99,
    canal_vendas: "Loja fisica",
    categoria: "Vestuario",
    descricao: "Roupas de alta qualidade",
    estoque: 200,
    avaliacao: 4.5,
    data_lancamento: new Date("2024-05-10")
  }
]);

// Coleção de Empresas
db.empresa.insertMany([
  {
    id_empresa: 1,
    nome_empresa: "Tech Innovations Inc.",
    cnpj: "12.345.678/0001-90",
    email: "contact@techinnovations.com",
    data_registro: new Date("2022-10-10"),
    setor: "Tecnologia",
    endereco: "Rua A, 123",
    telefone: "1234-5678",
    site: "https://techinnovations.com",
    pais: "Brasil"
  },
  {
    id_empresa: 2,
    nome_empresa: "Eco Solutions Ltd.",
    cnpj: "23.456.789/0001-01",
    email: "contato@empresaB.com",
    data_registro: new Date("2021-08-05"),
    setor: "Varejo",
    endereco: "Rua B, 456",
    telefone: "8765-4321",
    site: "help@ecosolutions.com",
    pais: "Brasil"
  }
]);

// Coleção de Campanhas
db.campanha.insertMany([
  {
    id_campanha: 1,
    nome_campanha: "Tech Expo 2024",
    data_registro: new Date("2024-06-15"),
    detalhes: "Apresentando o que ha de mais moderno em tecnologia.",
    status: "Ativa",
    objetivo: "Aumentar vendas",
    orcamento: 5000.00,
    duracao_campanha: "3 meses",
    id_empresa: 1,
    id_produto: 1,
    publico_alvo: "Jovens",
    principais_canais: ["Instagram", "Facebook"]
  },
  {
    id_campanha: 2,
    nome_campanha: "Fique em forma",
    data_registro: new Date("2024-07-20"),
    detalhes: "Equipamento de fitness inovador para todas as suas necessidades.",
    status: "Inativa",
    objetivo: "Aumentar reconhecimento de marca",
    orcamento: 3000.00,
    duracao_campanha: "2 meses",
    id_empresa: 2,
    id_produto: 2,
    publico_alvo: "Adultos",
    principais_canais: ["Twitter", "LinkedIn"]
  }
]);
// Coleção de Assinaturas de Empresas 
db.assinaturas_empresas.insertMany([
  {
    id_assinatura: 1,
    valor_assinatura: 200.00,
    data_inicio: new Date("2024-01-01"),
    data_fim: new Date("2025-01-01"),
    status: "Ativo",
    id_empresa: 1,
    tipo_plano: "Mensal",
    metodo_pagamento: "Cartao",
    nivel_suporte: "Premium",
    renovacao_automatica: true,  

  },
  {
    id_assinatura: 2,
    valor_assinatura: 150.00,
    data_inicio: new Date("2024-02-01"),
    data_fim: new Date("2025-02-01"),
    status: "Inativo",
    id_empresa: 2,
    tipo_plano: "Anual",
    metodo_pagamento: "Boleto",
    nivel_suporte: "Basico",
    renovacao_automatica: false, 

    }
]);

// Coleção de Históricos de Pagamento
db.historico_pagamentos.insertMany([
  {
    id_historico: 1,
    valor_pagamento: 100.00,
    data_pagamento: new Date("2024-03-10"),
    data_vencimento: new Date("2024-03-01"),
    nota_fiscal: "NotaFiscal123",
    id_assinatura: 1,
    metodo: "Cartao",
    status: "Pago",
    taxa_juros: 1.5,                
    desconto_aplicado: 10.00,       
    descricao_transacao: "Assinatura mensal do plano Premium" 
  },
  {
    id_historico: 2,
    valor_pagamento: 80.00,
    data_pagamento: new Date("2024-04-15"),
    data_vencimento: new Date("2024-04-10"),
    nota_fiscal: "NotaFiscal456",
    id_assinatura: 2,
    metodo: "Boleto",
    status: "Atrasado",
    taxa_juros: 2.0,                 
    desconto_aplicado: 5.00,         
    descricao_transacao: "Assinatura anual do plano Basico"   
  }
]);


// Coleção de Usuários
db.usuario_perfil.insertMany([
  {
    id_usuario: 1,
    nome_usuario: "John Doe",
    senha_usuario: "admin123",
    data_registro: new Date("2024-02-05"),
    permissao_usuario: "Admin",
    status: "Ativo",
    id_empresa: 1,
    cargo: "Administrador",
    ultimo_login: new Date("2024-10-22"),
    departamento: "TI"
  },
  {
    id_usuario: 2,
    nome_usuario: "Jane Smith",
    senha_usuario: "user123",
    data_registro: new Date("2024-03-15"),
    permissao_usuario: "Usuario",
    status: "Inativo",
    id_empresa: 2,
    cargo: "Usuario",
    ultimo_login: new Date("2024-09-20"),
    departamento: "Marketing"
  }
]);

// Coleção de Métodos de Pagamento
db.metodo_pagamento.insertMany([
  {
    nome_metodo: "Cartao de Credito",
    id_historico: 1,
    id_assinatura: 1,
    data_pagamento: new Date("2024-10-01"),
    status_pagamento: "Completo",
    id_transacao: "TRX123456",
    moeda: "BRL",
    valor_pago: 120.00,
    notas: "Pagamento de assinatura mensal",
    detalhes_metodo: {
      tipo_cartao: "Visa",
      ultimos_quatro_digitos: "1234",
      validade: "2026-04"
    }
  },
  {
    nome_metodo: "Cartao de Debito",
    id_historico: 2,
    id_assinatura: 2,
    data_pagamento: new Date("2024-09-15"),
    status_pagamento: "Pendente",
    id_transacao: "TRX654321",
    moeda: "BRL",
    valor_pago: 150.00,
    notas: "Assinatura anual",
    detalhes_metodo: {
      nome_banco: "Banco do Brasil",
      tipo_conta: "Corrente",
      agencia: "001",
      numero_conta: "123456-7"
    }
  }
]);

