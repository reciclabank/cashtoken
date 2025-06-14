import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def get_supabase_client() -> Client:
    """
    Retorna uma instância do cliente Supabase.
    
    Returns:
        Client: Cliente Supabase configurado
    """
    return supabase
