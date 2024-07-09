from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.get('/')
def inicio():
    """
    :return: Mensagem de inicio na api.
    """

    response = {
        "Success": 200,
        "Message": "API de Cadastro de Pessoas com integração ao banco de dados PostgreSQL funcionando perfeitamente.",
        "Versão": 1.0,
        "Info": (
            "Esta API oferece funcionalidades completas para o gerenciamento de cadastros de pessoas e imagens, "
            "incluindo operações de criação, leitura, atualização e exclusão. Desenvolvida com FastAPI, a aplicação "
            "garante desempenho e segurança. O processo de deploy é automatizado através do GitHub Actions, que "
            "gera e publica a imagem Docker no Docker Hub, seguida de implantação na plataforma Render."
        ),
        "Arquitetura": (
            "Arquitetura limpa (Clean Architecture) foi adotada para garantir a separação de responsabilidades e "
            "facilidade de manutenção. O projeto é estruturado em camadas, incluindo camadas de apresentação, domínio, "
            "aplicação e infraestrutura."
        ),
        "Bibliotecas Principais": (
            "FastAPI, Psycopg2, Pydantic, Pytest para testes, e Docker para containerização."
        ),
        "Padrões de Design": (
            "O projeto utiliza vários padrões de design, incluindo Repository Pattern para abstração da camada de acesso "
            "a dados, e Dependency Injection para gerenciamento de dependências."
        ),
        "Boas Práticas": (
            "Boas práticas de desenvolvimento foram seguidas, incluindo a escrita de testes unitários e de integração, "
            "validação rigorosa de dados de entrada e saída com Pydantic, e documentação automática com Swagger. "
            "Além disso, o código é versionado e revisado continuamente para garantir qualidade e robustez."
        ),
        "Documentação": "Utilize '(link)/docs' para acessar a documentação completa via Swagger.",
        "Desenvolvedor": "Carlos Eduardo dos S. Padilha"
    }

    return response

