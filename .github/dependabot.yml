version: 2  

updates:  

  # Configuração para dependências de Python (requirements.txt)  
  - package-ecosystem: "pip"  # Usa pip para gerenciar dependências  
    directory: "/"              # Diretório do projeto  
    schedule:  
      interval: "weekly"        # Atualiza semanalmente  
    commit-message:  
      prefix: "fix"             # Prefixo da mensagem de commit  
      

  # Configuração para dependências de JavaScript (package.json)  
  - package-ecosystem: "npm"  
    directory: "/"  # Diretório onde está o package.json  
    schedule:  
      interval: "weekly"  # Verificações semanais  
    commit-message:  
      prefix: "fix"  # Prefixo na mensagem de commit  
      include: "scope"  # Inclui o nome da dependência na mensagem  
    versioning-strategy: "auto"  # Estratégia de versão
