# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True, editable = False
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class DimConselho(models.Model):
    idconselho = models.AutoField(primary_key=True)
    nmconselho = models.CharField(max_length=50, blank=True, null=True)
    descconselho = models.CharField(max_length=50, blank=True, null=True)
    numregistro = models.CharField(max_length=10, blank=True, null=True)
    nmestado = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_conselho'


class DimConsulta(models.Model):
    idconsulta = models.AutoField(primary_key=True)
    dim_motivo_idmotivo = models.ForeignKey('DimMotivo', models.DO_NOTHING, db_column='dim_motivo_idmotivo')
    dim_medico_dim_especialidade_idespecialidade = models.IntegerField()
    dim_medico_dim_conselho_idconselho = models.IntegerField()
    dim_medico_idmedico = models.ForeignKey('DimMedico', models.DO_NOTHING, db_column='dim_medico_idmedico')
    dim_medico_dim_prestador_idprestador = models.IntegerField()
    dim_medico_dim_tipo_funcionario_idtipo_funcionario = models.IntegerField()
    dim_medico_dim_tipo_funcionario_dim_funcao_idfuncao = models.IntegerField()
    nmconsulta = models.CharField(max_length=50, blank=True, null=True)
    dtconsulta = models.DateField(blank=True, null=True)
    dim_exames = models.CharField(max_length=50, blank=True, null=True)
    qtdexames = models.IntegerField(blank=True, null=True)
    anammese = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_consulta'
        unique_together = (('idconsulta', 'dim_motivo_idmotivo', 'dim_medico_dim_especialidade_idespecialidade', 'dim_medico_dim_conselho_idconselho', 'dim_medico_idmedico', 'dim_medico_dim_prestador_idprestador', 'dim_medico_dim_tipo_funcionario_idtipo_funcionario', 'dim_medico_dim_tipo_funcionario_dim_funcao_idfuncao'),)


class DimEndereco(models.Model):
    idendereco = models.AutoField(primary_key=True)
    nmendereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    nmbairro = models.CharField(max_length=255, blank=True, null=True)
    nmcidade = models.CharField(max_length=255, blank=True, null=True)
    nmestado = models.CharField(max_length=255, blank=True, null=True)
    nmpais = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=255, blank=True, null=True)
    nmcomplento = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_endereco'


class DimEnderecoCep(models.Model):
    idendereco_cep = models.AutoField(primary_key=True)
    nmcep = models.CharField(max_length=100, blank=True, null=True)
    nm_enereco = models.CharField(max_length=100, blank=True, null=True)
    nmbairro = models.CharField(max_length=100, blank=True, null=True)
    nmcidade = models.CharField(max_length=100, blank=True, null=True)
    nmestado = models.CharField(max_length=100, blank=True, null=True)
    nmobservacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_endereco_cep'


class DimEspecialidade(models.Model):
    idespecialidade = models.AutoField(primary_key=True)
    nmespecialidade = models.CharField(max_length=20, blank=True, null=True)
    nmdescricao = models.CharField(max_length=20, blank=True, null=True)
    observacao = models.CharField(max_length=20, blank=True, null=True)
    dtregistro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_especialidade'


class DimExames(models.Model):
    idexames = models.AutoField(primary_key=True)
    dtexame = models.DateField(blank=True, null=True)
    dtcoleta = models.DateField(blank=True, null=True)
    dtresultado = models.DateField(blank=True, null=True)
    nmexame = models.CharField(max_length=50, blank=True, null=True)
    nmobservacao = models.CharField(max_length=50, blank=True, null=True)
    idconsulta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dim_exames'


class DimFuncao(models.Model):
    idfuncao = models.AutoField(primary_key=True)
    nmcargo = models.CharField(max_length=20, blank=True, null=True)
    dtcadastro = models.DateField(blank=True, null=True)
    nmobservacao = models.CharField(max_length=20, blank=True, null=True)
    num_cat_trabalho = models.CharField(max_length=20, blank=True, null=True)
    serie = models.CharField(max_length=20, blank=True, null=True)
    num_pis_pasep = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_funcao'


class DimMedico(models.Model):
    idmedico = models.AutoField(primary_key=True)
    dim_prestador_idprestador = models.ForeignKey('DimPrestador', models.DO_NOTHING, db_column='dim_prestador_idprestador')
    dim_tipo_funcionario_idtipo_funcionario = models.ForeignKey('DimTipoFuncionario', models.DO_NOTHING, db_column='dim_tipo_funcionario_idtipo_funcionario')
    dim_conselho_idconselho = models.ForeignKey(DimConselho, models.DO_NOTHING, db_column='dim_conselho_idconselho')
    dim_especialidade_idespecialidade = models.ForeignKey(DimEspecialidade, models.DO_NOTHING, db_column='dim_especialidade_idespecialidade')
    dim_tipo_funcionario_dim_funcao_idfuncao = models.IntegerField()
    dtcadastro = models.DateField(blank=True, null=True)
    observacao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_medico'
        unique_together = (('idmedico', 'dim_prestador_idprestador', 'dim_tipo_funcionario_idtipo_funcionario', 'dim_conselho_idconselho', 'dim_especialidade_idespecialidade', 'dim_tipo_funcionario_dim_funcao_idfuncao'),)


class DimMotivo(models.Model):
    idmotivo = models.AutoField(primary_key=True)
    nmmotivo = models.CharField(max_length=20, blank=True, null=True)
    nmobservacao = models.CharField(max_length=20, blank=True, null=True)
    dtmotivo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_motivo'


class DimPessoa(models.Model):
    idpessoa = models.AutoField(primary_key=True)
    dim_endereco_cep_idendereco_cep = models.ForeignKey(DimEnderecoCep, models.DO_NOTHING, db_column='dim_endereco_cep_idendereco_cep')
    dim_tipo_pessoa_idtipo_pessoa = models.ForeignKey('DimTipoPessoa', models.DO_NOTHING, db_column='dim_tipo_pessoa_idtipo_pessoa')
    nmpessoa = models.CharField(max_length=50, blank=True, null=True)
    dtcadastro = models.DateField(blank=True, null=True)
    nmobservacao = models.CharField(max_length=50, blank=True, null=True)
    nm_numero = models.CharField(max_length=50, blank=True, null=True)
    nmcomplemento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_pessoa'
        unique_together = (('idpessoa', 'dim_endereco_cep_idendereco_cep', 'dim_tipo_pessoa_idtipo_pessoa'),)


class DimPrestador(models.Model):
    idprestador = models.AutoField(primary_key=True)
    nmprestador = models.CharField(max_length=20, blank=True, null=True)
    dtcadastro = models.DateField(blank=True, null=True)
    nmobservacao = models.CharField(max_length=20, blank=True, null=True)
    cnpj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dtregistro = models.DateField(blank=True, null=True)
    nmjunta_comercial = models.CharField(max_length=20, blank=True, null=True)
    nmestado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_prestador'


class DimTipoFuncionario(models.Model):
    idtipo_funcionario = models.AutoField(primary_key=True)
    dim_funcao_idfuncao = models.ForeignKey(DimFuncao, models.DO_NOTHING, db_column='dim_funcao_idfuncao')
    nmtipo_funcionario = models.CharField(max_length=20, blank=True, null=True)
    dtregistro = models.DateField(blank=True, null=True)
    dtcontratacao = models.DateField(blank=True, null=True)
    nmclassificacao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_tipo_funcionario'
        unique_together = (('idtipo_funcionario', 'dim_funcao_idfuncao'),)


class DimTipoPessoa(models.Model):
    idtipo_pessoa = models.AutoField(primary_key=True)
    nmpfisica = models.CharField(max_length=25, blank=True, null=True)
    nmpjuridica = models.CharField(max_length=25, blank=True, null=True)
    dtcadastro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_tipo_pessoa'





class FatoAtendimento(models.Model):
    idatendimento = models.AutoField(primary_key=True)
    dim_endereco_idendereco = models.ForeignKey(DimEndereco, models.DO_NOTHING, db_column='dim_endereco_idendereco')
    dim_consulta_idconsulta = models.ForeignKey(DimConsulta, models.DO_NOTHING, db_column='dim_consulta_idconsulta')
    dim_pessoa_idpessoa = models.ForeignKey(DimPessoa, models.DO_NOTHING, db_column='dim_pessoa_idpessoa')
    dim_tipo_funcionario_idtipo_funcionario = models.ForeignKey(DimTipoFuncionario, models.DO_NOTHING, db_column='dim_tipo_funcionario_idtipo_funcionario')
    dim_tipo_funcionario_dim_funcao_idfuncao = models.IntegerField()
    dim_consulta_dim_medico_dim_tipo_funcionario_dim_funcao_idfunca = models.IntegerField()
    dim_consulta_dim_medico_dim_tipo_funcionario_idtipo_funcionario = models.IntegerField()
    dim_consulta_dim_medico_dim_prestador_idprestador = models.IntegerField()
    dim_consulta_dim_medico_idmedico = models.IntegerField()
    dim_consulta_dim_medico_dim_conselho_idconselho = models.IntegerField()
    dim_consulta_dim_medico_dim_especialidade_idespecialidade = models.IntegerField()
    dim_consulta_dim_motivo_idmotivo = models.IntegerField()
    dim_pessoa_dim_tipo_pessoa_idtipo_pessoa = models.IntegerField()
    dim_pessoa_dim_endereco_cep_idendereco_cep = models.IntegerField()
    idconsulta = models.IntegerField()
    idpaciente = models.IntegerField(blank=True, null=True)
    dtatendimento = models.DateField(blank=True, null=True)
    idatendente = models.IntegerField(blank=True, null=True)
    nmatendimento = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fato_atendimento'
        unique_together = (('idatendimento', 'dim_endereco_idendereco', 'dim_consulta_idconsulta', 'dim_pessoa_idpessoa', 'dim_tipo_funcionario_idtipo_funcionario', 'dim_tipo_funcionario_dim_funcao_idfuncao', 'dim_consulta_dim_medico_dim_tipo_funcionario_dim_funcao_idfunca', 'dim_consulta_dim_medico_dim_tipo_funcionario_idtipo_funcionario', 'dim_consulta_dim_medico_dim_prestador_idprestador', 'dim_consulta_dim_medico_idmedico', 'dim_consulta_dim_medico_dim_conselho_idconselho', 'dim_consulta_dim_medico_dim_especialidade_idespecialidade', 'dim_consulta_dim_motivo_idmotivo', 'dim_pessoa_dim_tipo_pessoa_idtipo_pessoa', 'dim_pessoa_dim_endereco_cep_idendereco_cep'),)



