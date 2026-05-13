# 🌐 Como Atualizar o Dashboard via GitHub Web

Como tokens podem expirar ou se perder, a forma mais prática e segura é usar o editor direto do GitHub Web para fazer atualizações sem precisar de acesso ao terminal.

## 📋 Opção 1: Editar arquivo existente

### Para editar index.html ou outro arquivo:

1. Acesse: https://github.com/CristianodeSouza/curi
2. 2. Clique no arquivo que deseja editar (ex: index.html)
   3. 3. Clique no ícone ✏️ (lápis) no canto superior direito
      4. 4. Faça as alterações necessárias
         5. 5. Role até o final da página
            6. 6. Clique em **"Commit changes..."**
               7. 7. Adicione uma mensagem descritiva no formato:
                  8.    - `fix:` para correções
                        -    - `feat:` para novas funcionalidades
                             -    - `docs:` para documentação
                                  -    - Exemplo: "fix: corrigir encoding de caracteres especiais"
                                       - 8. Deixe selecionado "Commit directly to the main branch"
                                         9. 9. Clique em "Commit changes"
                                           
                                            10. ## 📄 Opção 2: Criar novo arquivo
                                           
                                            11. ### Para adicionar um novo arquivo (como data.json):
                                           
                                            12. 1. Acesse: https://github.com/CristianodeSouza/curi
                                                2. 2. Clique em **"Add file"** (botão verde)
                                                   3. 3. Selecione **"Create new file"**
                                                      4. 4. No campo "Name your file...", digite o nome completo:
                                                         5.    - Exemplo: `data.json` ou `src/dados.json`
                                                               - 5. Cole o conteúdo no editor
                                                                 6. 6. Role até o final
                                                                    7. 7. Clique em **"Commit new file"**
                                                                       8. 8. Adicione uma mensagem descritiva
                                                                          9. 9. Deixe selecionado "Commit directly to the main branch"
                                                                             10. 10. Clique em "Commit new file"
                                                                                
                                                                                 11. ## 🔄 Fluxo de Atualização Completo
                                                                                
                                                                                 12. ### Exemplo: Adicionar arquivo de dados JSON
                                                                                
                                                                                 13. 1. **Criar data.json**:
                                                                                     2.    ```json
                                                                                              {
                                                                                                "atendimentos": [
                                                                                                  {
                                                                                                    "id": 1,
                                                                                                    "descricao": "Atendimento 1",
                                                                                                    "status": "aberto"
                                                                                                  }
                                                                                                ]
                                                                                              }
                                                                                              ```

                                                                                           2. **Atualizar index.html** para usar o arquivo:
                                                                                           3.    - Procure por: `async function loadData()`
                                                                                                 -    - Modifique para fazer fetch do `data.json`
                                                                                                      -    - Commit com mensagem: "feat: integrar dados via arquivo JSON"
                                                                                                       
                                                                                                           - 3. **Verificar no GitHub Pages**:
                                                                                                             4.    - Acesse: https://cristianodesouza.github.io/curi/
                                                                                                                   -    - Aguarde 1-2 minutos para a atualização ser publicada
                                                                                                                        -    - Limpe cache: Ctrl+Shift+Delete (ou Cmd+Shift+Delete no Mac)
                                                                                                                             -    - Recarregue a página: Ctrl+F5
                                                                                                                              
                                                                                                                                  - ## ⚡ Dicas e Boas Práticas
                                                                                                                              
                                                                                                                                  - ### Mensagens de Commit
                                                                                                                              
                                                                                                                                  - Use o padrão "Conventional Commits":
                                                                                                                                  - - `feat:` Nova funcionalidade
                                                                                                                                    - - `fix:` Correção de bug
                                                                                                                                      - - `docs:` Documentação
                                                                                                                                        - - `style:` Formatação
                                                                                                                                          - - `refactor:` Refatoração de código
                                                                                                                                            - - `test:` Testes
                                                                                                                                              - - `chore:` Tarefas administrativas
                                                                                                                                               
                                                                                                                                                - Exemplos:
                                                                                                                                                - ```
                                                                                                                                                  feat: adicionar filtro por data
                                                                                                                                                  fix: corrigir encoding de acentos
                                                                                                                                                  docs: atualizar README com instruções
                                                                                                                                                  ```
                                                                                                                                                  
                                                                                                                                                  ### Antes de fazer commit
                                                                                                                                                  
                                                                                                                                                  1. **Verifique a sintaxe**:
                                                                                                                                                  2.    - JSON: Use https://jsonlint.com/ se necessário
                                                                                                                                                        -    - JavaScript: Procure por erros na aba "Code"
                                                                                                                                                             -    - HTML: O GitHub destaca erros automaticamente
                                                                                                                                                              
                                                                                                                                                                  - 2. **Teste a mudança**:
                                                                                                                                                                    3.    - Faça o commit
                                                                                                                                                                          -    - Aguarde 2-3 minutos
                                                                                                                                                                               -    - Visite a página do GitHub Pages
                                                                                                                                                                                    -    - Limpe o cache do navegador
                                                                                                                                                                                         -    - Verifique se tudo está funcionando
                                                                                                                                                                                          
                                                                                                                                                                                              - 3. **Se houver erro**:
                                                                                                                                                                                                4.    - Volta ao arquivo
                                                                                                                                                                                                      -    - Clique em ✏️ para editar
                                                                                                                                                                                                           -    - Faça a correção
                                                                                                                                                                                                                -    - Faça um novo commit: "fix: corrigir erro anterior"
                                                                                                                                                                                                                 
                                                                                                                                                                                                                     - ## 🐛 Resolvendo Problemas Comuns
                                                                                                                                                                                                                 
                                                                                                                                                                                                                     - ### Página não atualiza após commit
                                                                                                                                                                                                                 
                                                                                                                                                                                                                     - 1. Aguarde 2-3 minutos (GitHub Pages demora para fazer deploy)
                                                                                                                                                                                                                       2. 2. Limpe cache do navegador:
                                                                                                                                                                                                                          3.    - Windows: Ctrl+Shift+Delete
                                                                                                                                                                                                                                -    - Mac: Cmd+Shift+Delete
                                                                                                                                                                                                                                     - 3. Recarregue a página: Ctrl+F5 (ou Cmd+Shift+R no Mac)
                                                                                                                                                                                                                                       4. 4. Se ainda não funcionar, verifique em:
                                                                                                                                                                                                                                          - https://github.com/CristianodeSouza/curi/actions (CI/CD status)
                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                          - ### Arquivo com erro de sintaxe
                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                          - 1. Se o commit falhar:
                                                                                                                                                                                                                                            2.    - Verifique a aba "Blame" na página do arquivo
                                                                                                                                                                                                                                                  -    - Procure pela linha com erro (GitHub marca em vermelho)
                                                                                                                                                                                                                                                       -    - Edite novamente com a correção
                                                                                                                                                                                                                                                            -    - Faça um novo commit
                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                 - ### Caracteres especiais incorretos
                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                 1. Certifique-se de que o arquivo está em UTF-8:
                                                                                                                                                                                                                                                                 2.    - Ao criar arquivo, o GitHub usa UTF-8 por padrão
                                                                                                                                                                                                                                                                       -    - Se importar de outro lugar, verifique a codificação
                                                                                                                                                                                                                                                                            - 2. Para JSON com acentos:
                                                                                                                                                                                                                                                                              3.    ```json
                                                                                                                                                                                                                                                                                       {
                                                                                                                                                                                                                                                                                         "mensagem": "Olá, bem-vindo!",
                                                                                                                                                                                                                                                                                         "status": "Em Aberto"
                                                                                                                                                                                                                                                                                       }
                                                                                                                                                                                                                                                                                       ```
                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                    ## 📚 Recursos Úteis
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                - [Editor do GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files-in-your-repository)
                                                                                                                                                                                                                                                                                - - [Commits no GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files)
                                                                                                                                                                                                                                                                                  - - [GitHub Pages](https://pages.github.com/)
                                                                                                                                                                                                                                                                                    - - [Conventional Commits](https://www.conventionalcommits.org/)
                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                      - ## ✅ Checklist antes de fazer Deploy
                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                      - - [ ] Arquivo criado/editado com sucesso
                                                                                                                                                                                                                                                                                        - [ ] - [ ] Sintaxe do arquivo está correta
                                                                                                                                                                                                                                                                                        - [ ] - [ ] Mensagem de commit é descritiva
                                                                                                                                                                                                                                                                                        - [ ] - [ ] Commit foi realizado na branch `main`
                                                                                                                                                                                                                                                                                        - [ ] - [ ] Aguardei 2-3 minutos para o GitHub Pages atualizar
                                                                                                                                                                                                                                                                                        - [ ] - [ ] Limpei o cache do navegador (Ctrl+Shift+Delete)
                                                                                                                                                                                                                                                                                        - [ ] - [ ] Recarreguei a página (Ctrl+F5)
                                                                                                                                                                                                                                                                                        - [ ] - [ ] Verifiquei o resultado no navegador
                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                        - [ ] ---
                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                        - [ ] **Última atualização**: 13 de maio de 2026
                                                                                                                                                                                                                                                                                        - [ ] **Status**: ✅ Guia Completo para Atualizações via Web
