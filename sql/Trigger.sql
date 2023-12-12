CREATE OR REPLACE FUNCTION upar_jogador_trigger()
RETURNS TRIGGER AS $upar_jogador_trigger$
DECLARE
    vida_jogador INT;
    ataque_jogador INT;
    res_jogador INT;
    novo_vida INT;
    novo_ataque INT;
    novo_res INT;
BEGIN
    

    SELECT
        Vida, Ataque, Resistencia
    INTO
        vida_jogador, ataque_jogador, res_jogador
    FROM
        Jogador
    WHERE
        Id_Jogador = NEW.Id_Jogador;

    
    novo_vida := vida_jogador + 10;
    novo_ataque := ataque_jogador + 5;
    novo_res := res_jogador + 1;

    
    UPDATE Jogador
    SET Vida = novo_vida, Ataque = novo_ataque, Resistencia = novo_res
    WHERE Id_Jogador = NEW.Id_Jogador;

    RETURN NEW;
END;
$upar_jogador_trigger$ LANGUAGE plpgsql;


CREATE TRIGGER trigger_upar_jogador
AFTER UPDATE ON Jogador
FOR EACH ROW
EXECUTE FUNCTION upar_jogador_trigger();