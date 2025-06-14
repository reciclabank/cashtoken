import os
import json
from src.config.supabase import get_supabase_client

def migrate_collection_requests():
    """
    Migra os dados de solicitações de coleta dos arquivos JSON para o Supabase.
    
    Este script lê o arquivo collection_requests.json e insere os dados na tabela
    collection_requests do Supabase.
    """
    # Obter cliente Supabase
    supabase = get_supabase_client()
    
    # Caminho para o arquivo JSON
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                            '..', 'static', 'data', 'collection_requests.json')
    
    try:
        # Verificar se o arquivo existe
        if not os.path.exists(json_file):
            print(f"Arquivo não encontrado: {json_file}")
            return False
        
        # Ler dados do arquivo JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            collection_requests = json.load(f)
        
        print(f"Lidos {len(collection_requests)} registros do arquivo JSON")
        
        # Inserir dados no Supabase
        for request in collection_requests:
            # Remover o campo 'id' se existir, pois o Supabase gerará automaticamente
            if 'id' in request:
                request_id = request.pop('id')
                # Opcional: manter o ID original em um campo separado
                request['original_id'] = request_id
            
            # Inserir no Supabase
            result = supabase.table('collection_requests').insert(request).execute()
            
            # Verificar se a inserção foi bem-sucedida
            if hasattr(result, 'error') and result.error:
                print(f"Erro ao inserir registro: {result.error}")
            else:
                print(f"Registro inserido com sucesso: {request.get('name')}")
        
        print("Migração de solicitações de coleta concluída com sucesso!")
        return True
    
    except Exception as e:
        print(f"Erro durante a migração: {str(e)}")
        return False

def migrate_prices():
    """
    Migra os dados de preços dos arquivos JSON para o Supabase.
    
    Este script lê o arquivo prices.json e insere os dados na tabela
    materials e prices do Supabase.
    """
    # Obter cliente Supabase
    supabase = get_supabase_client()
    
    # Caminho para o arquivo JSON
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                            '..', 'static', 'data', 'prices.json')
    
    try:
        # Verificar se o arquivo existe
        if not os.path.exists(json_file):
            print(f"Arquivo não encontrado: {json_file}")
            return False
        
        # Ler dados do arquivo JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            prices_data = json.load(f)
        
        print(f"Lidos dados de preços do arquivo JSON")
        
        # Inserir materiais e preços no Supabase
        for category, materials in prices_data.items():
            for material_name, price in materials.items():
                # Primeiro, inserir ou obter o material
                material_result = supabase.table('materials').select('id').eq('name', material_name).execute()
                
                if len(material_result.data) == 0:
                    # Material não existe, criar
                    material_data = {
                        'name': material_name,
                        'category': category
                    }
                    material_insert = supabase.table('materials').insert(material_data).execute()
                    material_id = material_insert.data[0]['id']
                else:
                    # Material já existe
                    material_id = material_result.data[0]['id']
                
                # Agora, inserir o preço
                price_data = {
                    'material_id': material_id,
                    'price': price,
                    'date': 'now()'  # Função SQL para data atual
                }
                
                price_result = supabase.table('prices').insert(price_data).execute()
                
                print(f"Preço inserido para {material_name}: R$ {price}")
        
        print("Migração de preços concluída com sucesso!")
        return True
    
    except Exception as e:
        print(f"Erro durante a migração de preços: {str(e)}")
        return False

def migrate_purchases():
    """
    Migra os dados de compras dos arquivos JSON para o Supabase.
    
    Este script lê o arquivo purchases.json e insere os dados na tabela
    purchases do Supabase.
    """
    # Obter cliente Supabase
    supabase = get_supabase_client()
    
    # Caminho para o arquivo JSON
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                            '..', 'static', 'data', 'purchases.json')
    
    try:
        # Verificar se o arquivo existe
        if not os.path.exists(json_file):
            print(f"Arquivo não encontrado: {json_file}")
            return False
        
        # Ler dados do arquivo JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            purchases = json.load(f)
        
        print(f"Lidos {len(purchases)} registros de compras do arquivo JSON")
        
        # Inserir dados no Supabase
        for purchase in purchases:
            # Remover o campo 'id' se existir, pois o Supabase gerará automaticamente
            if 'id' in purchase:
                purchase_id = purchase.pop('id')
                # Opcional: manter o ID original em um campo separado
                purchase['original_id'] = purchase_id
            
            # Inserir no Supabase
            result = supabase.table('purchases').insert(purchase).execute()
            
            # Verificar se a inserção foi bem-sucedida
            if hasattr(result, 'error') and result.error:
                print(f"Erro ao inserir compra: {result.error}")
            else:
                print(f"Compra inserida com sucesso: {purchase.get('date')}")
        
        print("Migração de compras concluída com sucesso!")
        return True
    
    except Exception as e:
        print(f"Erro durante a migração de compras: {str(e)}")
        return False

if __name__ == "__main__":
    print("Iniciando migração de dados para o Supabase...")
    
    # Migrar solicitações de coleta
    print("\n=== Migrando solicitações de coleta ===")
    migrate_collection_requests()
    
    # Migrar preços
    print("\n=== Migrando preços de materiais ===")
    migrate_prices()
    
    # Migrar compras
    print("\n=== Migrando registros de compras ===")
    migrate_purchases()
    
    print("\nProcesso de migração concluído!")
